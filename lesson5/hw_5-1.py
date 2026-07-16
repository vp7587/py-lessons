import string,keyword, sys
print("Program will check if string is a correct name for a variable")
while True:
    use_var_allow = False
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        raw_string = input("Please enter string (min length is 1, max raw string length is 254).\n")
        if len(raw_string) < 1 or len(raw_string) > 254:
            print("Sorry, your sting is too short or too long. \n"
                  "Ensure sting len more then 0 ang less then 254 and try again.")
        else:
            raw_string_list = list(raw_string)
            EXCLUDE_PUNCTUATION_RAW = "".join(list(string.punctuation))
            EXCLUDE_PUNCTUATION = EXCLUDE_PUNCTUATION_RAW.replace("_", " ")
            EXCLUDE_NAMES = keyword.kwlist
            #use system names check
            if raw_string in EXCLUDE_NAMES:
                print("\nSorry, var string is not allowed to use this program (EXCLUDE_NAMES).\n")
                continue
            #use special symbols check
            for char in raw_string_list:
                if char in EXCLUDE_PUNCTUATION:
                    print("\nSorry, this string is not allowed to use this program (EXCLUDE_PUNCTUATION or has space).\n")
                    continue
            # __ and ___ check
            underscore_list = ("__","___")
            if raw_string in underscore_list:
                print("\nSorry, var string is not allowed to because of using __ or ___ or space .\n")
                continue
            for char in raw_string_list:
                if char in string.ascii_uppercase:
                    print("\nSorry, var string is not allowed. (To upper char is not allowed).\n")
                    continue
            if raw_string_list[0].isdigit():
                print("\nSorry, var string is not allowed. First char cant be number.\n")
                continue
        use_var_allow = True
        print(f"Is allowed to use sting as var state: {use_var_allow}\n")
    else:
        print("Good bye.")
        sys.exit()
