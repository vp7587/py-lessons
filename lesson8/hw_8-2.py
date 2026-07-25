import sys,string

print("The program checks, if string is palindrome")

def is_palindrome(text):
    text = text.lower().strip().replace(" ", "")
    for i in text:
        if i in string.punctuation:
            text = text.replace(i,"")
    reversed_text = "".join(list(reversed(text)))
    if reversed_text == text:
        return True
    else:
        return False

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        case_1 = "A man, a plan, a canal: Panama"
        case_2 = "0P"
        case_3 = "a."
        case_4 = "aurora"
        print(f"Cases to test are:\n\ncase 1: {case_1},\ncase 2: {case_2},\ncase 3: {case_3},\ncase 4: {case_4}")
        assert is_palindrome(case_1) == True, 'Test1'
        assert is_palindrome(case_2) == False, 'Test2'
        assert is_palindrome(case_3) == True, 'Test3'
        assert is_palindrome(case_4) == False, 'Test4'
        # is_palindrome('A man, a plan, a canal: Panama')
        print("\nAll tests are done.")
    else:
        print("Good bye.")
        sys.exit()