from functions import *
import csv
from datetime import datetime
from gtts import gTTS

language = 'en'
import os
import sys


# FUNCTIONS THAT TAKE INPUT
def get_time(time, array) : # get month day year hour minutes and append into array

    array[0] = time.year
    array[1] = time.month
    array[2] = time.day
    array[3] = time.hour
    array[4] = time.minute

def levels(array): # get level input from user
    level = input("Input your levels: ")
    array[5] = int(level)

def focus_rating(array): # get focus rating input from user
    focus = input("Input your focus rate: ")
    array[6] = int(focus)

def food(array): # get food input from user
    food = input("Input the food you ate: ")
    array[7] = food

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
        
# FUNCTIONS THAT OUTPUT
def send_data (filename, arr): # tasked with sending data to dataset.csv

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(arr)

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

main() # start the process