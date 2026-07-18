import sys
print("Program will convert your number of seconds to a sting with days and time.")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        user_string = input("Please enter integer number between 0 and 8640000.\n")
        #length check
        if 1 > len(user_string):
            print("\nError: you enter less then 1 symbol. Try again\n")
            continue
        #is digit check
        if (user_string.isdigit() == False):
            print("\nError: you should put only digits.\n")
            continue
        time = int(user_string)
        #value check
        if  0 < time < 8640000 == False:
            print("\nError: your number is not between 0 and 8640000.\n")
            continue
        days = time // 86400
        hours = str(time % 86400 // 3600)
        minutes = str(time % 86400 % 3600 // 60)
        seconds = str(time % 86400 % 3600 % 60)
        #decide to print "days" or ""days
        if  days % 2 != 0:
            days_quantity = "day"
        else:
            days_quantity = "days"
        print (f"Your time is: {days} {days_quantity}, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}.")
    else:
        print("Good bye.")
        sys.exit()