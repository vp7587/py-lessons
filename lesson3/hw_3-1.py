from encodings import undefined

print("The program makes operation chosen operation (+|-|*|/) with 2 numbers.\nPlease, follow the instructions below")
number_1 = float(input("Please enter the first number:\n"))
number_2 = float(input("Please enter the second number:\n"))
operation = input("Please chose on operation. Correct values are +, -, *, /\n")
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
            print("Sorry,division by0 is not allowed")
        else:
            result = number_1 / number_2
print(f"The result is: {result}.")

