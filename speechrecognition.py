#import
import speech_recognition as sr

AUDIO_FILE = ("speech_ntm.wav")

#initialise the recognizer
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)        #reads the audio file

try:
    print("Audio File Contents : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition didn't get it.")
except sr.RequestError:
    print("Couldn't get the results from gsr")

