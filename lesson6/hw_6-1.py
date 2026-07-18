import sys, string
print("Program show alphabet letter between users letters.")
while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        user_string = str.strip(input("Please enter 2 letter, devined by space. Example: a-d.\n"))
        user_string_list = list(user_string)
        #length check
        if len(user_string) != 3:
            print("\nError: wrong data. You should enter 3 symbols like this: a-d. Try again\n")
            continue
        #is current values check
        if user_string[0].isalpha() == False or user_string[1] != "-" or user_string[2].isalpha() == False :
            print("\nError: your input is not in correct format. Example: a-d.\n")
            continue
        ASCII_LETTERS = string.ascii_letters
        #print(ASCII_LETTERS)
        start_position = 0
        end_position = 0
        for i in ASCII_LETTERS:
            if i == user_string[0]:
                #print (ASCII_LETTERS.index(i))
                start_position = ASCII_LETTERS.index(i)+1
        for i in ASCII_LETTERS:
            if i ==user_string[2]:
                #print (ASCII_LETTERS.index(i))
                end_position = ASCII_LETTERS.index(i)
        if start_position > end_position:
            print(f"Success. Final string is: {ASCII_LETTERS[start_position-2:end_position:-1]}\n", end="")
        else:
            print(f"Success. Final string is: {ASCII_LETTERS[start_position:end_position]}\n", end="")
        continue
    else:
        print("Good bye.")
        sys.exit()