import sys
print("Program will make product of numbers in string until result is not less or equal than 9")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        user_string = input("Please enter integer number (min length is 1.\n")
        #length check
        if len(user_string) < 1:
            print("Sorry, your number is less then 1. Try again\n")
            continue
        #is digit check
        if (user_string.isdigit() == False):
            print("Please enter integer number with min length = 1.\n")
            continue
        list_user_string = list(user_string)
        #start calculating
        round = 1
        while len(list_user_string)  > 1:
            #print(f"Current number is: {list_user_string}")
            result = 1
            for i in list_user_string:
                result *= int(i)
            print(f"Round {round} result: {result}")
            list_user_string = list(str(result))
            round += 1
        print(f"Final number is: {result}\n")
    else:
        print("Good bye.")
        sys.exit()
