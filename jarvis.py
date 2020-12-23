import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am anju. Please tell me how may i help you") 
    
def takeCommand():
    # it takes microphone input from the user and return string command
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1      
        audio=r.listen(source)  
    try:
        print("recogizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")  
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anjukashyap109@gmail.com','anju@123_')
    server.sendmail('anjukashya109p@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    # speak("anju is a good girl")
    wishMe()
    while True:
       query=takeCommand().lower()
    #logic for executing tasks based on query
       if 'wikipedia' in query:
           speak("searching wikipedia...")
           query=query.replace("wikipedia","")
           reuslts = wikipedia.summary(query,sentences=2)
           speak("acording to wikipedia")
           print(reuslts)
           speak(reuslts)
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       elif 'open google' in query:
            webbrowser.open("google.com")
       elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")   
    #    elif 'open stackoverflow' in query:
    #         webbrowser.open("stackoverflow.com")   
       elif 'play music' in query:
           music_dir="C:\\Users\\91913\\Desktop\\song"
           songs=os.listdir(music_dir)
           print(songs)
           c=random.choice([0,1,2,3,4,5,6,7,8,9,10])
           os.startfile(os.path.join(music_dir,songs[c])) 
       elif "the time " in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strtime}")
       elif "open pycharm" in query:
            code_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin"
            os.startfile(code_path)
       elif "email to anju" in query:
           try:
               speak("what should I say")
               content=takeCommand()
               to="komalkashyap810@gmail.com"
               sendemail(to,content)
               speak("email has been sent")
           except Exception as e:
                print(e)
                speak("sorry anju ,i am not able to send this email")        
                     
       break
        
         