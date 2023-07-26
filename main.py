import pyglet
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os
import pygame, time


def speak(maintext):
    if os.path.exists("welcome.mp3"):
        os.remove("welcome.mp3")

    # Language in which you want to convert
    language = 'en'

    myobj = gTTS(text=maintext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    pygame.init()
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.unload()

    # Playing the converted file
    # os.system("mpg321 welcome.mp3")
    # os.remove("welcome.mp3")


def func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Speak Anything")
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        s = ""
        try:
            text = r.recognize_google(audio)
            s = text
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
            speak("Sorry could not recognize what you said")

        # getting path
        chrome_path = r"/Applications/Google Chrome.app"

        # First registers the new browser
        webbrowser.register('chrome', None,
                            webbrowser.BackgroundBrowser(chrome_path))

        if s.find("Google") != -1:
            speak("Opening Google")
            webbrowser.get('chrome').open("http://google.com")
        elif s.find('YouTube') != -1:
            speak("Opening Youtube")
            webbrowser.get('chrome').open("http://youtube.com")
        elif s.find("spotify") != -1:
            speak("Opening Spotify")
            webbrowser.get('chrome').open("http://spotify.com")
        elif s.find("Facebook") != -1:
            speak("Opening Facebook")
            webbrowser.get('chrome').open("http://facebook.com")
        elif s.find("Twitter") != -1:
            speak("Opening Twitter")
            webbrowser.get('chrome').open("http://twitter.com")
        elif s.find("Instagram") != -1:
            speak("Opening Instagram")
            webbrowser.get('chrome').open("http://instagram.com")
        else:
            print("Couldnt recognise what you said\n\n")
            speak("Couldnt recognise what you said")
            func()


func()
