import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrary
import requests
import pyautogui
import cv2
import subprocess
import time
from dotenv import load_dotenv
import os
import openai
from gtts import gTTS
import sys
import keyboard
from datetime import datetime
from googletrans import Translator
import asyncio
import numpy as np
import pygame

api_key="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"
news_api ="0acbd280ea7f4d5b8f9c25eae2aa3fb5" 
weather_api = "6d677293066e8aac79e99b328d4bd5c4"
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    speech = gTTS(text=text, lang='en')
    speech.save("output.mp3")
    os.system("afplay output.mp3")
    os.remove("output.mp3")

def aiProcess(c):
    
    openai.api_key="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",


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return print(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening google sir,what you want to search on google sir")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for your command...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
       
        except sr.RequestError:
            print("Could not request results.")
        pyautogui.typewrite(command)
        keyboard.press('enter')
    

        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Openning facebook sir")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Openning youtube sir")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Openning linkedin sir")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "tell me the news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=bd&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            
            articles = data.get('articles',[])
           
            for article in articles:
                speak(article['title'])
        else:
            print("Someting wrong")

    elif "exit" in c.lower():
        speak("Closing this tab, sir")
        time.sleep(0.5) 
        keyboard.send('command+w')

    elif "open camera" in c.lower():
        speak("Opening camera sir")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            speak("Cannot open camera sir")
        

        while True:
            ret, frame = cap.read()
            if not ret:
                speak("Failed to capture frame sir")
                break
                
            cv2.imshow('Camera', frame)  # Display the camera feed.
                
                # Break the loop when 'q' is pressed.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()  # Release the camera resource.
        cv2.destroyAllWindows()  # Close all OpenCV windows.
    
    elif "open new tab" in c.lower():
        speak("New tab opening sir")
        time.sleep(0.5)
        keyboard.send('command+t')


    elif "open notepad" in c.lower():
        speak("Notepad Opening sir")
        subprocess.run(["open", "-a", "Notes"])
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for a command...")
            try:
                audio = recognizer.listen(source, timeout=10,phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print(f"Command recognized: {command}")
            
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
        
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
            if command:
                pyautogui.typewrite(command, interval=0.1)

    elif "type into terminal" in c.lower():
            speak("Typing into terminal sir")
            text_to_type = "Hi, i am riad. I build this project using fance language python, pyhton is really amazing when you import some module and it's improved me to be productive and learn python in new way"
            speak(text_to_type)
            pyautogui.typewrite(text_to_type, interval=0.1)  # Simulate typing.   

    elif "open photo" in c.lower():
    # Open Photo Booth
        subprocess.run(["osascript", "-e", 'tell application "Photo Booth" to activate'])
        speak("Opening Photo Booth, sir")
        time.sleep(2)  # Wait for Photo Booth to open
        speak("Smile sir")
    # Simulate taking a photo
        keyboard.send('command+shift+t')  # This triggers the "Take Photo" shortcut in Photo Booth
        speak("Photo taken successfully")
    
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com/")
        speak("Chat gpt is opening sir")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for your command...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
       
        except sr.RequestError:
            print("Could not request results.")
        pyautogui.typewrite(command)
        keyboard.send('enter')

    elif "how are you" in c.lower():
        speak("I am fine sir, what about you?")
    elif "i am fine" in c.lower():
        speak("It's really nice to talk with you sir")
    elif "take a screenshot" in c.lower():
        keyboard.send('enter+shift+command+3')
        speak("Screenshot taken successfully sir")
    elif "scroll down" in c.lower():
        keyboard.send('down arrow')
    elif "scroll up" in c.lower():
        keyboard.send('up arrow')
    elif "top of the page" in c.lower():
        keyboard.send('command+up arrow')
    elif "bottom of the page" in c.lower():
        keyboard.send('command+down arrow')
    elif "open apple tv" in c.lower():
            speak("Opening Apple TV,sir")
            subprocess.run(["osascript", "-e", 'tell application "TV" to activate'])
            speak("Apple TV is open now")
    elif "tell me the date" in c.lower():
        today = datetime.today().strftime("%A, %B %d, %Y")  
        speak(f"Today's date is {today}")
    elif "tell me the time" in c.lower():
        current_time = datetime.now().strftime("%I:%M %p") 
        speak(f"The current time is {current_time}")
    elif "tell me the weather" in c.lower():
        api_key = "6d677293066e8aac79e99b328d4bd5c4"
        city = "Gazipur"  
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
        complete_url = base_url + city + '&appid=' + api_key
     
        try:
            response = requests.get(complete_url)
            response.raise_for_status() 
            data = response.json()
            if data['cod'] == '404':
                speak("City not found.")
            else:
                maini = data['main']
                weather_desc = data['weather'][0]['description']
                temp = maini['temp'] - 273.15  
                speak(f"The current weather in {city} is {weather_desc} with a temperature of {temp:.2f}°C.")
        except requests.exceptions.RequestException as e:
            speak(f"An error occurred: {e}")

    elif "calculator mode" in c.lower():
        speak("Calculator mode is start sir")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for a command...")
            try:
                audio = recognizer.listen(source, timeout=10,phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print(f"Command recognized: {command}")
            
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
        
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
            result = eval(command)
            speak(f"The result is {result}")

    elif "translator mode" in c.lower():
        target_language='bn'
        text = "Hello, how are you?"
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        time.sleep(3)
        speak(f"The translation is: {translated.text}")

 
    elif "set volume" in c.lower():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:  # Ensure the microphone is properly initialized
            speak("Type terminal for the desired volume level, between 0 and 100.")
            

            try:
            
                
            # Validate and set the volume
                try:
                    volume_level = int(input())  # Convert the command to an integer
                    if 0 <= volume_level <= 100:
                        os.system(f"osascript -e 'set volume output volume {volume_level}'")
                        print(f"Volume set to {volume_level} percent.")
                        speak(f"Volume set to {volume_level} percent.")
                    else:
                        print("Volume must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please say a valid number.")
        
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that. Please try again.")
            except sr.RequestError as e:
                print(f"Could not process the request. Error: {e}")


    elif "mute" in c.lower():
        os.system("osascript -e 'set volume output muted true'")
    elif "unmute" in c.lower():
        os.system("osascript -e 'set volume output muted false'")

    elif "tell me my family details" in c.lower():
        speak('''Assalamualykum sir, 
              your name : Md. Al-Riyad
              your father name : Ahsan Habib sujon
              your mother name : Mst. Rezina
              your uncle name : Mofiur Rahman sumon
              your antey name : Shakhi
              your sister name : Samiya tabassum mou
              your bother name : Sabir hossain sad
              your grand father name : Abdul hamid mojnu
              your grand mother name : Mst. Fatima
              ''')
        print('''Assalamualykum sir, 
              your name : Md. Al-Riyad
              your father name : Ahsan Habib sujon
              your mother name : Mst. Rezina
              your uncle name : Mofiur Rahman sumon
              your antey name : Shakhi
              your sister name : Samiya tabassum mou
              your bother name : Sabir hossain sad
              your grand father name : Abdul hamid mojnu
              your grand mother name : Mst. Fatima ''')  
    elif "open python" in c.lower():
        speak("PyChram is opening sir")
        subprocess.run(["open", "-a", "PyCharm"])  

    elif "open whatsapp" in c.lower():
        speak("WhatsApp is opening sir")
        subprocess.run(["open", "-a", "WhatsApp"])
    elif "open espresso" in c.lower():
        speak("Espresso-c is opening sir")
        subprocess.run(["open", "-a", "Espresso-C"])
    elif "open arduino" in c.lower():
        speak("Arduion IDE is opening sir")
        subprocess.run["open","-a","Arduino IDE"]
    elif "open app store" in c.lower():
        speak("App store is opening sir")
        subprocess.run(["open","-a","App Store"])
    elif "open mail" in c.lower():
        speak("Mail is opening sir")
        subprocess.run(["open","-a","Mail"])
    elif "open calendar" in c.lower():
        speak("Calendar is opening sir")
        subprocess.run(["open","-a","Calendar"])
    elif "open reminders" in c.lower():
        speak("Reminders is opening sir")
        subprocess.run(["open","-a","Reminders"])
    elif "open facetime" in c.lower():
        speak("Face time is opening sir")
        subprocess.run(["open","-a","FaceTime"])
    elif "open map" in c.lower():
        speak("Map is opening sir")
        subprocess.run(["open","-a","Maps"])
    elif "open calculator" in c.lower():
        speak("Calculator is opening sir")
        subprocess.run(["open","-a","Calculator"])
    elif "open safari" in c.lower():
        speak("Safari browser is opening sir")
        subprocess.run(["open","-a","Safari"])
    elif "open safari" in c.lower():
        speak("Safari browser is opening sir")
        subprocess.run(["open","-a","Safari"])
    
    else:
        output = aiProcess(command)
        print(output)
        speak(output)


if __name__ == "__main__":
    speak("Hello sir, I am Olivia. How can i help you?")
    while True:
        r = sr.Recognizer()
        
        print("Listening .... ")

        try:
            with sr.Microphone() as source:
                print("Recognizing.....")
                audio = r.listen(source,timeout=10,phrase_time_limit=5)
                command = r.recognize_google(audio)
            print(command)
            if(command.lower() == "olivia"):
                speak("I am listenning sir")
                with sr.Microphone() as source:
                    print("Olivia active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
            
        except Exception as e:
            print("Error;{0}".format(e))












