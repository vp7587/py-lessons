import sys
print("The program will summ even elements of the list and multiply it on the last element of the list.\n")
run = "y"
while run == "y" or run == "Y"  or run == "YES" or run == "yes":
    run = str.lower(input("Would you like to continue?(Type y/yes if you do):\n"))
    if run == "y" or run == "yes":
        print("Please input a few numbers as string, to fill the list.\n")
        raw_text = input("Please enter a few numbers like this: 0123456\n")
        if raw_text:
            if raw_text.isdigit():
                numbers_list = list(raw_text)
                count_numbers_list_elements = len(numbers_list)
                print(f"Your list is: {numbers_list}. Ok. Going ahead..")
                if count_numbers_list_elements == 1:
                        print(f"Your has only one item")
                else:
                    #Непосредственное выполнение дз
                    i = 0
                    result = 0
                    summ = 0
                    for j in range(len(numbers_list)):
                        if j % 2 == 0:
                            # print(f"{numbers_list[j]} is even element")
                            summ = summ + int(numbers_list[j])
                            # print(f"The summ is: {summ}")
                        # else:
                            # print(f"{numbers_list[j]} is not even")
                    last_element_caption = int(numbers_list[-1])
                    print(f"The sum of even elements is {summ}. The last element is: {last_element_caption}")
                    result = summ * last_element_caption
                    print(f"The final result is: {result}")
            else:
                print("Sorry, invalid input. You should enter only numbers.")
        else:
            result = 0
            print(f"Your list is empty, so result: {result}")
    else:
        print("Exiting program... Good bye.")
        sys.exit()