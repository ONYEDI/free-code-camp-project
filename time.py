
def add_time(time,duration,week):
    #this is a simple add time class that is 

    # split the string into list
    time_list = time.split(" ")

    # splitting the durations into list
    duration_list = duration.split(":")

    # seperating the individual component of the list
    times = time_list[0].split(":")

    #creating list of days of the week
    weekday = ["sunday","monday","tuesday","wednesday","thursday"
    ,"friday","saturday"]
    
    #converting the string values into interger value
    times[0] = int(times[0])
    times[1] = int(times[1])
    duration_list[0] = int(duration_list[0])
    duration_list[1] = int(duration_list[1])
    

    # coverting the time into 24 hour clock format
    time_24 = []
    if time_list[1] =="am":
        time_24 = times 

    else:
        time_24.append(times[0]+12)
        time_24.append(times[1])

    
    # summing up the time and the time durations
    # for the hour 
    total_time_hour = time_24[0] + duration_list[0]

    # the minutes
    total_time_mins = time_24[1] + duration_list[1]

    # converting the total_time_mins to the base 60
    if total_time_mins > 59:
        total_time_hour += 1
        time_mins = total_time_mins % 60

    # getting the number of days
    if total_time_hour > 23:
        number_of_day = total_time_hour//24

        #getting the value of time in 12 hour clock
        time_1 = total_time_hour % 24
        time_2 = time_1 + times[0]
    
    #getting the index of the day of the week
    indec = weekday.index(week)

    # getting the present day of the week
    day = ((indec + number_of_day) % 7)

    #getting the timepriod like in pm and am
    if time_2 > 12:
        time_priod = "pm"
        time_12 = time_2 - 12
    else:
        time_priod = "am"
        time_12 = time_2

    # printing decisions
    if number_of_day == 1 :
        word = "next day"
    else:
        number_of_day = str(number_of_day)
        word = 'in next ' + number_of_day + " days"

    # doing type conversion 
    time_1 = str(time_1)
    time_mins = str(time_mins)
    time_priod = str(time_priod)
    weekday[day] =str( weekday[day])
    time_12 = str(time_12)


    # return values
    print( time_12 + ":" + time_mins + " " + time_priod +"," + weekday[day] + "("+ word +")")
    
     


# testing the function
add_time("5:34 pm","100:37","tuesday")
add_time("2:34 pm","36:37","monday")

