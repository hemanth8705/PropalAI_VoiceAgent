# PropalAI VoiceAgent

PropalAI VoiceAgent is a Python-based project designed to provide voice recognition and audio processing functionality.

## Features
- **Speech Recognition:** Convert speech to text.
- **Audio Processing:** Handle MP3 and WAV audio files.
- **Environment Configurations:** Uses a .env file for sensitive configurations.

## Setup

1. Clone the repository:
   ```
   git clone [REPOSITORY_URL]
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

## Workflow

1. **Branching Strategy:**
   - Create a new branch for each feature or bugfix:
     ```
     git checkout -b feature/your-feature-name
     ```
     
2. **Development:**
   - Make your changes and commit them with descriptive messages:
     ```
     git commit -am "Add feature X"
     ```
     
3. **Testing:**
   - Ensure all tests pass before pushing your changes:
     ```
     pytest
     ```
     
4. **Pull Requests:**
   - Push your branch to the remote repository:
     ```
     git push origin feature/your-feature-name
     ```
   - Open a pull request and describe your changes. Request reviews from team members.

5. **Merging:**
   - Once approved and all tests pass, merge your branch into the main branch.
   - Delete the feature branch after merging.

## Usage

- Ensure that you have the necessary environment variables set in the `.env` file.
- Run the main application:
  ```
  python VoiceAgent.py
  ```

## Testing

- Unit tests are located in the `tests` directory.
- Run tests using your preferred test runner (e.g., pytest):
  ```
  pytest
  ```

## License

This project is licensed under the MIT License.