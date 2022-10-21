from gtts import gTTS 
import os

def textToSpeech(): 
    someText = input("Enter some text: ")
    audio = gTTS(text = someText, lang = "pl", slow = False)

    audio.save("example.mp3") 
    os.system("start example.mp3")

textToSpeech() 