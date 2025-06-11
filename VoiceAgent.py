import streamlit as st
import sounddevice as sd
import soundfile as sf
import whisper
import numpy as np
import tempfile
import time
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from gtts import gTTS
from playsound import playsound
import re

# ========== TTS using gTTS ==========
import pygame

def speak_gtts_full(text):
    import tempfile
    import pygame
    from gtts import gTTS
    import time
    import os

    # Create a unique temp file and close it before TTS and playback
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_audio.close()  # IMPORTANT: Close it so gTTS and pygame can access it

    try:
        # Generate speech
        tts = gTTS(text=text, lang='en')
        tts.save(temp_audio.name)

        # Play using pygame
        pygame.mixer.init()
        pygame.mixer.music.load(temp_audio.name)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()

    finally:
        os.remove(temp_audio.name)  # Clean up the file


# ========== SETUP ==========
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
fs = 44100
channels = 1

# ========== Langchain Setup ==========
model = ChatGroq(model="Gemma2-9b-it", groq_api_key=groq_api_key)
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chat = RunnableWithMessageHistory(model, get_session_history)
config = {"configurable": {"session_id": "voice-chat"}}

# ========== Streamlit UI ==========
st.set_page_config(page_title="🎙️ AI Voice Chat", layout="centered")
st.title("🧠 Talk to AI (Voice Chatbot)")

# Session state setup
for key in ["is_recording", "start_time", "recording", "last_response", "chat_history", "user_text"]:
    if key not in st.session_state:
        st.session_state[key] = None if key == "user_text" else []

# Recording buttons
if not st.session_state.is_recording:
    if st.button("🎙️ Start Talking"):
        st.session_state.is_recording = True
        st.session_state.start_time = time.time()
        st.session_state.recording = sd.rec(int(600 * fs), samplerate=fs, channels=channels)
        st.info("Recording... Speak now!")
else:
    if st.button("⏹️ Stop & Chat"):
        st.session_state.is_recording = False
        sd.stop()

        duration = int(time.time() - st.session_state.start_time)
        audio_data = st.session_state.recording[:duration * fs]

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            sf.write(temp_audio.name, audio_data, fs)

            with st.spinner("🧠 Transcribing your voice..."):
                whisper_model = whisper.load_model("base")
                result = whisper_model.transcribe(temp_audio.name)
                user_text = result["text"]
                st.session_state.user_text = user_text
                st.success("🗣️ You said:")
                st.write(f"**You**: {user_text}")

                # Send to LLM
                with st.spinner("🤖 Thinking..."):
                    response = chat.invoke([HumanMessage(content=user_text)], config=config)
                    bot_text = response.content
                    print(f"AI Response: {bot_text}")
                    st.session_state.last_response = bot_text

# Show progressive text + synced TTS
# Show AI response and speak it fully before showing text
if st.session_state.last_response:
    st.subheader("🤖 AI:")
    bot_text = st.session_state.last_response
    display_area = st.empty()

    # Speak the entire response first
    speak_gtts_full(bot_text)

    # Then show it
    display_area.markdown(f"**AI**: {bot_text}")



# Save chat history (optional future display)
st.session_state.chat_history.append(("You", st.session_state.user_text))
st.session_state.chat_history.append(("AI", st.session_state.last_response))
