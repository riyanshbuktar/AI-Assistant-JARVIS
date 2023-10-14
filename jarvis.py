import pyttsx3
import datetime
import speech_recognition as sr
import smtplib

engine = pyttsx3.init()

def speak (audio):
    engine.say (audio)
    engine.runAndWait()

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(command)
for token in doc:
    print(token.text, token.pos_, token.dep_)


def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Riyansh Sir, I hope you are doing good!")
    speak("The Time Now is")
    time()
    speak("Todays date is")
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Riyansh Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Riyansh Sir!!")

    elif hour>=18 and hour<24:
        speak("Good Evening Riyansh Sir!")

    else:
        speak("Have a Good Night Riyansh Sir!")
                
    speak("Jarvis at your Service . Please tell me How may I Help you!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Riyansh sir Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

wishme()
takeCommand()



















