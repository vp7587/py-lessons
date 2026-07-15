import sys
print("The program makes chosen operation (+|-|*|/) with 2 numbers."
      "\nPlease, follow the instructions below")
while True:
    run_program = str.strip(str.lower(input("Would you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        number_1 = input("Please enter the first number:\n")
        number_2 = input("Please enter the second number:\n")
        if not (number_1.isdigit() or number_1.isdigit()):
            print("Sorry, invalid numbers. Please, type only numbers")
        else:
            operation = input("Please choose on operation. Correct values are: +, -, *, /\n")
            if operation not in ["+", "-", "*", "/"]:
                print("Sorry, invalid operation. Please, type only : +, -, *, /")
            else:
                number_1 = int(number_1)
                number_2 = int(number_2)
                result = "undefined"
                match operation:
                    case "+":
                        result = number_1 + number_2
                    case "-":
                        result = number_1 - number_2
                    case "*":
                        result = number_1 * number_2
                    case "/":
                        if number_2 == 0:
                            print("Sorry, division by 0 is not allowed operation")
                        else:
                            result = number_1 / number_2
                print(f"The result is: {result}.")
    else:
        print("Good bye.")
        sys.exit()