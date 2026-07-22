import sys,string

print("The program corrects inputed string, making the first char capital if it is lower and adds point in the end if it is missed ) ")

def correct_string (def_string):
    exclude_punctuation = "".join(list(string.punctuation))
    def_string = list(def_string)
    if def_string[0] in exclude_punctuation:
        def_result = "Error. The first char should be special symbol"
        return result
    if not def_string[0].isdigit():
        def_string[0] = phrase[0].upper()
    else:
        def_result = f"Error. The first char should not be digit {def_string[0]}"
        return def_result
    if def_string[-1] != ".":
        def_string.append(".")
    return "".join(list(def_string))


while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        phrase = input("\nInput your string\n").strip()
        result = correct_string(phrase)
        assert result[0].isupper() and result[-1] == ".", 'check name and age'
        print(result)
    else:
        print("Good bye.")
        sys.exit()