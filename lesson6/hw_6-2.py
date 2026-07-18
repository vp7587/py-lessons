import sys
print("Program will convert your number of seconds to a sting with days and time.")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        user_string = input("Please enter integer number between 0 and 8640000.\n")
        #length check
        if 0 < len(user_string) < 8640000:
            print("\nError: you enter less then 1 symbol. Try again\n")
            continue
        #is digit check
        if (user_string.isdigit() == False):
            print("\nError: you should put only digits.\n")
            continue

    else:
        print("Good bye.")
        sys.exit()