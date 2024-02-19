# Jarvis_001
Chatbot - Jarvis voice assistant
Sure! Let's break down the code step by step:

1. **Importing Libraries**:
   - `speech_recognition`: This library provides functions to recognize speech from audio input.
   - `pyttsx3`: This library allows the Python interpreter to access text-to-speech engines.
   - `os`: This module provides a portable way of using operating system-dependent functionality.
   - `openai`: This library provides access to OpenAI's GPT models and other APIs.
   - `dotenv`: This library loads variables from a .env file into the environment.

2. **Loading OpenAI API Key**:
   - The `load_dotenv()` function loads environment variables from a .env file into the environment.
   - `os.getenv('OPENAI_API_KEY')` retrieves the OpenAI API key from the environment variable.

3. **Setting OpenAI API Key**:
   - `openai.api_key = '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'` sets the OpenAI API key for authentication.

4. **Initializing Text-to-Speech Engine**:
   - `pyttsx3.init()` initializes the text-to-speech engine.

5. **Function to Convert Text to Speech**:
   - `speak(text)`: This function takes a text input and uses the text-to-speech engine to speak it out loud.

6. **Function to Recognize Speech from Microphone**:
   - `recognize_speech()`: This function listens to audio input from the microphone, recognizes speech using Google's speech recognition service, and returns the recognized text.

7. **Function to Interact with OpenAI API**:
   - `chat_with_openai(prompt)`: This function interacts with OpenAI's GPT model to generate responses based on the user's input prompt. It sends the user's prompt to the GPT model and retrieves the generated response.

8. **Main Function**:
   - `main()`: This function serves as the entry point of the program. It starts by greeting the user and then enters a loop where it listens to the user's voice input, recognizes it, sends it to the OpenAI model for processing, retrieves the response, and speaks it out loud using the text-to-speech engine. The loop continues until the user says "exit".

9. **Execution**:
   - `if __name__ == "__main__": main()`: This line ensures that the `main()` function is executed only if the script is run directly, not if it is imported as a module into another script.

Overall, this code creates a simple voice assistant that listens to the user's voice input, recognizes it, sends it to OpenAI's GPT model to generate a response, and then speaks the response back to the user.
