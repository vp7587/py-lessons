import string,keyword, sys
print("Program will check if string is a correct name for a variable")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        raw_string = input("Please enter string (min length is 1, max raw string lenght is 254).\n")
        if len(raw_string) < 1 or len(raw_string) > 254:
            print("Sorry, your sting is too short or too long. \n"
                  "Ensure sting len more then 0 ang less then 254 and try again.")
        else:
            raw_string_list = list(raw_string)
            EXCLUDE_PUNCTUATION_RAW = "".join(list(string.punctuation))
            EXCLUDE_PUNCTUATION = EXCLUDE_PUNCTUATION_RAW.replace("_", "")
            EXCLUDE_NAMES = keyword.kwlist
            if raw_string in EXCLUDE_NAMES:
                print("\nSorry, var name is not allowed to use this program (EXCLUDE_NAMES).\n")
            else:
                for char in raw_string_list:
                    if char in EXCLUDE_PUNCTUATION:
                        print("\nSorry, var name is not allowed to use this program (EXCLUDE_PUNCTUATION).\n")
                        break

    else:
        print("Good bye.")
        sys.exit()
