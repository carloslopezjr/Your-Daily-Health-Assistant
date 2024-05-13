from functions import *

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

        levels(arr) # ask them to check their moring gluclose level

        focus_rating(arr) # ask how they feel from 1 - 10

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