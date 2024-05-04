from functions import send_data

# once the sensor is registered, we want to check the time of day
from datetime import datetime

# if time is in between 7am - 11am and it's the first time they passed through, then we want to greet them
time = datetime.now()
times_passed = 0 # this is the amount of times the sensor has registered

if times_passed == 0:
    print("Good morning Sir, I hope you had good sleep, it is time to do your daily health check.")
    times_passed += 1

    send_data()

    # ask how they feel from 1 - 10
    # ask them to check their moring gluclose level
    # give them the stats for the previous day and week

else:
    print("How's it going sir, did you want to do a quick health check?")
    times_passed += 1

    # how do you currently feel fomr 1 - 10
    # what did you eat anything for breakfast?
        # what did you eat?
        # at what time
        # what's your current blood sugar level
    
    # did you eat anything else?
        # repeat questions
    
    # I see that it's lunch/dinner time, did you plan on eating again?

    # alright that's all I needed, talk soon

# then have times_passed reset whenever 3 am hits


# what is the total amount of data you want?

    # focus r8
    # levels
    # food if applicable
    # month
    # day
    # year
    # hour
    # minutes