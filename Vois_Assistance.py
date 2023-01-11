import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time 
import os

def sptext():
    reco=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        reco.adjust_for_ambient_noise(source)
        audio=reco.listen(source)
        try:
            print("recognizing...")
            data=reco.recognize_google(audio)
            return data
        except sr.UnknowValueError:
            print(" Not Understand ")
def speechtx(x):
    engin=pyttsx3.init()
    voice=engin.getProperty('voices')
    engin.setProperty('voice',voice[0].id)
    rate=engin.getProperty('rate')
    engin.setProperty('rate',150)
    engin.say(x)
    engin.runAndWait()
if __name__=='__main__':
    if sptext().lower()=="hello alexa":
        t="How may i help You?"
        speechtx(t)
        time.sleep(5)
        while True:
            data1=sptext().lower()
            if "your name" in data1:
                name="my name is Alexa"
                speechtx(name)
            elif " old are you" in data1:
                age="i am twenty year old"
                speechtx(age)
            elif 'time' in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif " joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                speechtx(joke_1)
            elif 'play song' in data1:
                add="D:\Music"
                listsong=os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))
            elif "exit" in data1:
                speechtx("Thanks you")
                break
            time.sleep(10)
