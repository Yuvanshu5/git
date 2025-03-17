import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  

    speak("Hii yuvanshu  sir, I am Daannaav. Please tell me how may I help you")

def takeCommand():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open ai tool' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'open iiit raichur' in query:
            webbrowser.open("https://iiitr.ac.in/")  
        
        elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps")

        # elif 'play music' in query:
        #     webbrowser.open("https://open.spotify.com/")

        elif 'play  music' in query:
            music_dir = 'C:\\Users\\DELL\\Music\\MEmu Music'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the directory.")
            else:
                speak("Music directory not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("VS Code not found.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            print("No query matched")
