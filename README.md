# PropalAI VoiceAgent

PropalAI VoiceAgent is a Python-based project designed to provide voice recognition and audio processing functionality.

## Features
- **Speech Recognition:** Convert speech to text.
- **Audio Processing:** Handle MP3 and WAV audio files.
- **Environment Configurations:** Uses a .env file for sensitive configurations.


This project is an **AI Voice Chatbot** powered by:

- 🎙️ **Speech-to-Text** via OpenAI Whisper
- 🧠 **LLM Responses** from Groq (Gemma 2B or 9B)
- 🔊 **Text-to-Speech (TTS)** using gTTS and Pygame
- 🌐 Frontend built with **Streamlit**

---

## 🔄 Workflow: Data & Request Flow

### 1. 🎤 Voice Input
- User clicks **"Start Talking"**
- Audio is recorded using `sounddevice`
- Recording runs in real time until **"Stop & Chat"** is clicked

---

### 2. 🔊 Recording Handling
- Audio is saved temporarily as a `.wav` file via `soundfile`
- Audio snippet is trimmed based on actual speaking time

---

### 3. 🧠 Speech-to-Text (Whisper)
- Whisper model transcribes the audio into text
- Output is stored and displayed like:  
  `🗣️ You said: <transcribed-text>`

---

### 4. 🚀 Sending Text to LLM
- Transcribed text is sent to the **Groq LLM** using LangChain
- Chat memory is managed with `ChatMessageHistory`
- Model used: `Gemma-2b-it` or `Gemma-9b-it`
- LLM returns a full response in natural language

---

### 5. 🗣️ Text-to-Speech (TTS)
- The full LLM output is converted to voice using `gTTS`
- Audio is played using `pygame.mixer`
- Text is revealed only *after* speech playback finishes

---

### 6. 🧾 UI & Chat Log
- Conversation is displayed in the Streamlit frontend
- Session state keeps track of inputs and responses
- Messages are stored in `st.session_state.chat_history`

---

## 🧬 Component-Level Breakdown

| Component            | Technology            | Role                                   |
|---------------------|-----------------------|----------------------------------------|
| UI / Frontend       | Streamlit             | Controls recording and displays chat   |
| Audio Input         | sounddevice           | Records mic input                      |
| Audio Save          | soundfile             | Saves input as .wav                    |
| Transcription       | Whisper (base model)  | Converts audio to text                 |
| LLM Response        | LangChain + Groq      | Generates response from Gemma model    |
| Audio Playback      | gTTS + Pygame         | Speaks LLM output                      |
| Session Management  | Streamlit `session_state` | Maintains chat context               |

---


## Setup

1. Clone the repository:
   ```
   git clone https://github.com/hemanth8705/PropalAI_VoiceAgent.git
   ```
2. Change to the project directory:
   ```
   cd PropalAI_VoiceAgent
   ```
3. Create a virtual environment and activate it:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```


## Usage

- Ensure that you have the necessary environment variables set in the `.env` file.
- Run the main application:
  ```
  streamlit run VoiceAgent.py
  ```

## Testing

- Unit tests are located in the `tests` directory.
- Run tests using your preferred test runner (e.g., pytest):
  ```
  pytest
  ```

## License

This project is licensed under the MIT License.