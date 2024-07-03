from functions import *
from contextlib import redirect_stderr
import io


def microphone_names():
    # f = io.StringIO()
    # with redirect_stderr(f):
    #     r = sr.Recognizer()
    #     mic_list = sr.Microphone.list_microphone_names()

    # print("Available microphones:")
    # for index, name in enumerate(mic_list):
    #     print(f"{index}: {name}") 



# Code that works with right microphone, use microphone_names() to find what device_index to use
r = sr.Recognizer()
r.energy_threshold = 500
r.pause_threshold = 0.5
with sr.Microphone(device_index = 1) as source:
    print("Say something!")
    audio = r.listen(source)
    

try:
    print("We think you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("We didn't recognize the audio")
except sr.RequestError:
    print("Could not request results from Google")


