#translate speach to text and text to speech
import speech_recognition as sr
import pyttsx3
from openai import Completion
import os

OPENAI_KEY = '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'
import openai
openai.api_key  = OPENAI_KEY

#function to converet text to speech
def speaktext(command):
    #initialize the engine
    engine =  pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#initialize the recognizer
r = sr.Recognizer()

def record_text():
    #loop in case of errors
    while(1):
        try:
            #use the microphone as source for input
            with sr.Microphone() as source2:
                #prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration = 0.2)
                print("I am listening")
                #listens for the users input
                audio2 = r.listen(source2)
                #using google to recognize audio
                mytext = r.recognize_google(audio2)
                return mytext
        
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError as e:
            print("unknown error occured")

def send_to_chatgpt(messages, model="gpt-4"):
    response = Completion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].messages)
    return message


messages = [{"role": "user", "content": "Act like jarvise from Iron man and call me sam"}]
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatgpt(messages)
    speaktext(response)

    print(response)