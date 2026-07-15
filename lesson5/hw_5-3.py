import sys, string

print("Program will do the hashtag from the string")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        raw_string = input("Please enter string (min length is 1, max raw string lenght is 254).\n"
                           "IMPORTANT! Max hashtag length is 140. More simbols will cut):\n")
        if len(raw_string) < 1 or len(raw_string) > 254:
            print("Sorry, your sting is too short or too long. \n"
                  "Ensure sting len more then 0 ang less then 254 and try again.")
        else:
            raw_string_list = list(raw_string)
            #Remove special characters
            for character in raw_string_list:
                if character in string.punctuation:
                    raw_string_list.remove(character)
            normalized_string = "".join(raw_string_list)
            to_title_string = normalized_string.title()
            #Make each word to title
            to_title_string_list = list(to_title_string)
            #Remove spaces
            for char in to_title_string_list:
                if char == " ":
                    to_title_string_list.remove(char)
            #Insert hash in start
            to_title_string_list.insert(0, "#")
            #Cut to 140 simbols
            to_title_string_list = to_title_string_list[:140]
            final_hash_string = "".join(to_title_string_list)
            print(final_hash_string)
    else:
        print("Good bye.")
        sys.exit()

