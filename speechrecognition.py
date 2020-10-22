#import the module
import speech_recognition as sr

#import the audiofile...(.wav and .af)
AUDIO_FILE = ("speech_ntm.wav")

#initialise the recognizer
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    #reads the audio file
    audio = r.record(source)        

#convert
try:
    print("Audio File Contents : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition didn't get it.")
except sr.RequestError:
    print("Couldn't get the results from gsr")

