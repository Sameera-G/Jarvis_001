import speech_recognition as sr
import pyttsx3
import os
import openai
from dotenv import load_dotenv

# Load OpenAI API key from environment variable
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

# Set OpenAI API key
openai.api_key = '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'

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech from microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

# Function to interact with OpenAI API
def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # Use the appropriate engine here
        max_tokens=150,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": ""}
        ]
    )

    try:
        assistant_message = response.choices[0].message.content.strip()
        print("Assistant's response:", assistant_message)  # For debugging
        return assistant_message
    except Exception as e:
        print("Error accessing assistant's message:", e)
        print("Response object:", response)
        return "I'm sorry, but I couldn't process your request at the moment."

# Main function
def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = recognize_speech()
        if query:
            if query.lower() == "exit":
                speak("Goodbye!")
                break
            response = chat_with_openai(query)
            speak(response)

if __name__ == "__main__":
    main()
