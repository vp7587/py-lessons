raw_text= input("Please enter a few numbers like this: 123456\n")
if raw_text:
    if raw_text.isdigit():
        numbers_list = list(raw_text)
        count_numbers_list_elements = len(numbers_list)
        print(f"Your list consists of {count_numbers_list_elements}")
        print(f"Raw numbers list: {numbers_list}")
        print(f"The last element is: {numbers_list[-1]}")
        print("Lets make it the first element...")
        numbers_list.insert(0, numbers_list[-1])
        numbers_list.pop()
        print(f"New numbers list: {numbers_list}")
    else:
        print("Sorry, invalid input. You should enter only numbers.")
else:
    print("Your list is empty")



