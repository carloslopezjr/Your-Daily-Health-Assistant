import csv
from datetime import datetime
from gtts import gTTS
import os
import sys
import speech_recognition as sr
language = 'en'

# Get current time
def get_time(time, array) : # get month day year hour minutes and append into array

    array[0] = time.year
    array[1] = time.month
    array[2] = time.day
    array[3] = time.hour
    array[4] = time.minute

# Ask user for glucose levels & send to array
def levels(array):

    levels_message = "Insert levels message"
    # Function that expects a voice input
    input_message = voice_recognition(levels_message)

    # Test code 
    # print(input_message)
    
    # Send to array
    array[5] = int(input_message)

# Ask user for focus rating & send to array
def focus_rating(array):

    focus_message = "Insert focus message"

    # Function that expects a voice input
    input_message = voice_recognition(focus_message)
    
    # Test code
    # print(input_message)
    
    # Send to array
    array[6] = int(input_message)

# Ask user for food ate & send to array
def food(array): 
    food_message = "Insert food message"

    # Function that expects a voice input
    input_message = voice_recognition(food_message)

    # Test code
    # print(input_message)

    # Send to array
    array[7] = food

# Looks for specified microphone, reads voice input
def voice_recognition(question_message):
    
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

        voice_message(question_message, 'mac')
        audio = r.listen(source)

    # Create while loop to keep going until it reads something
    # recognize speech using Google
    try:
        message = "Google thinks you said " + r.recognize_google(audio)
        voice_message(message, 'mac')
        return r.recognize_google(audio)
        
    except sr.UnknownValueError:

        message = "Google could not understand audio, can you repeat it again?"
        voice_message(message, 'mac')

    except sr.RequestError as e:
        print("Google error; {0}".format(e))


# Functions for output

# Send data to csv
def send_data (filename, arr):

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(arr)


# Creates mp3 file for specified operation system
def voice_message(message, operation_system):

    if operation_system == 'mac':

        myobj = gTTS(text=message, lang='en', slow=False)
        myobj.save("/Users/carlos/Desktop/Your-Daily-Health-Assistant-1/data/voice_outputs/message.mp3")

        # mac version
        os.system("afplay /Users/carlos/Desktop/Your-Daily-Health-Assistant-1/data/voice_outputs/message.mp3")
    elif operation_system == 'windows':

        print('insert windows process')
        # windows version
        # os.system("start morning_message-v1.mp3")
    else:
        print("error, terminating program")
        sys.exit(1)

# Start the program
def main():
    # if time is in between 7am - 11am and it's the first time they passed through, then we want to greet them
    time = datetime.now()
    times_passed = 0 # this is the amount of times the sensor has registered

    if times_passed == 0:

        morning_text = "Insert Morning Message-v2"
        voice_message(morning_text, 'mac')
        
        times_passed += 1

        filename = '/Users/carlos/Desktop/Your-Daily-Health-Assistant-1/data/dataset.csv' # change whenever you clone in a different location
        
        # 'C:\\Users\\bravo\\Desktop\\Your-Daily-Health-Assistant-2\\data\\dataset.csv'

        # hold values before pushed to the csv
        arr = [0, 0, 0, 0, 0, 0, 0, 0]

        get_time(time, arr) # function that checks the current time to adjust voice prompt
            # example: voice-prompt: I see that it's lunch/dinner time, did you plan on eating again?

        levels_message = "Insert levels message"
        voice_message(levels_message, 'mac')

        levels(arr) # ask them to check their moring gluclose level

        focus_message = "Insert focus message"
        voice_message(focus_message, 'mac')

        focus_rating(arr) # ask how they feel from 1 - 10

        food_message = "Insert food message"
        voice_message(food_message, 'mac')

        food(arr) # ask for their food

        send_data(filename, arr)


        # give them the stats for the previous day and week

        # end with exit message
        completion_message = "Data upload completed. I will check-in soon!"
        voice_message(completion_message, 'mac')

    else:
        check_in = "Insert check-in message"
        voice_message(check_in, 'mac')
        times_passed += 1

    # then have times_passed reset whenever 3 am hits