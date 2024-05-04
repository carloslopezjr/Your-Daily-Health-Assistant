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
        writer.writerows()