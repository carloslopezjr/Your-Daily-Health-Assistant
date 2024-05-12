import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
# r.energy_threshold = 300


# List available microphones
'''
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")
'''


m = None
for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    if microphone_name == "External Microphone":
        m = sr.Microphone(device_index=i)


with m as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google
try:
    print("Google thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))

