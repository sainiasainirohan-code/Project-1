import speech_recognition as sr
import pyttsx3


a = sr.Recognizer()
engine=pyttsx3.init()
while True:
    with sr.Microphone() as source:
        print("listining...")
        audio = a.listen(source)

    try:
        text = a.recognize_google(audio)
        print(text)
        engine.say(text)
        engine.runAndWait()
        if "exit" in text:
                print("Exiting program...")
                engine.say("Exiting program")
                engine.runAndWait()
                break
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Could not request results; check your internet connection")