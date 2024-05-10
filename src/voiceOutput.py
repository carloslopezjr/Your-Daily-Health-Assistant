from functions import *
import csv
from datetime import datetime

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

# FUNCTIONS THAT OUTPUT
def send_data (filename, arr): # tasked with sending data to dataset.csv

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(arr)

def main():
    # if time is in between 7am - 11am and it's the first time they passed through, then we want to greet them
    time = datetime.now()

    times_passed = 0 # this is the amount of times the sensor has registered

    if times_passed == 0:
        print("Good morning Sir, I hope you had good sleep, it is time to do your daily health check.")
        times_passed += 1

        filename = 'C:\\Users\\bravo\\Desktop\\Your-Daily-Health-Assistant-2\\data\\dataset.csv' # change whenever you clone in a different location

        # hold values before pushed to the csv
        arr = [0, 0, 0, 0, 0, 0, 0, 0]

        get_time(time, arr)
        levels(arr) # ask them to check their moring gluclose level
        focus_rating(arr) # ask how they feel from 1 - 10
        food(arr) # ask for their food

        # what did you eat anything for breakfast?
            # what did you eat?
            # at what time
            # what's your current blood sugar level

        # I see that it's lunch/dinner time, did you plan on eating again?

        send_data(filename, arr)

        # give them the stats for the previous day and week

        # end with exit message



    else:
        print("How's it going sir, did you want to do a quick health check?")
        times_passed += 1

    # then have times_passed reset whenever 3 am hits


# call the main function
main()