from gtts import gTTS 
import os

def textToSpeech(): 
    try: 
        someText = input("Enter some text: ")
        language = input("Enter your language code: ")
        audio = gTTS(text = someText, lang = language, slow = False)

        audio.save("example.mp3") 
        os.system("start example.mp3")
    except: 
        print("An error occured")

textToSpeech() 