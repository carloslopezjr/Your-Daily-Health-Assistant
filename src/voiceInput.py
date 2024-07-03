from functions import *
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
# r.energy_threshold = 300


# List available microphones

print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

'''
m = None
for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    if microphone_name == "External Microphone":
        m = sr.Microphone(device_index=i)


with m as source:

    voice_message(message, 'mac')
    audio = r.listen(source)


# Create while loop to keep going until it reads something
# recognize speech using Google
try:
    message = "Google thinks you said " + r.recognize_google(audio)
    voice_message(message, 'mac')
    
except sr.UnknownValueError:

    message = "Google could not understand audio, can you repeat it again?"
    voice_message(message, 'mac')

except sr.RequestError as e:
    print("Google error; {0}".format(e))

'''