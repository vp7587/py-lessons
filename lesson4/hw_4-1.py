# i = 5
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         print(i)
#         # continue
#
#     if i % 3 == 0:
#         break




print("The program will move all zero from the list to the end of the list.\n")
run = "y"
while run == "y" or run == "Y"  or run == "YES" or run == "yes":
    print("Would you like to continue?(Type y/yes if you do):")
    run = input();
    if run == "y" or run == "Y" or run == "YES" or run == "yes":
        print("You should input a few numbers as string, including zero (0).\n")
        raw_text= input("Please enter a few numbers like this: 0123456\n")
        if raw_text:
            if raw_text.isdigit():
                numbers_list = list(raw_text)
                count_numbers_list_elements = len(numbers_list)
                print(f"Your list is not empty. Ok. Going ahead..")
                if count_numbers_list_elements == 1:
                    print(f"Your has only one item")
                else:
                    count_zero_in_list =  numbers_list.count("0")
                    if count_zero_in_list == 0:
                        print(f"Sorry, your list has no zero.")
                    else:
                        print(f"Well, your list has {count_zero_in_list} zeros. Going ahead..")
                        i = 0
                        while i < count_zero_in_list:
                            index_of_zero_in_list = numbers_list.index("0")
                            numbers_list.remove("0")
                            numbers_list.append("0")
                            i += 1
                        print(f"The final list is: {numbers_list}")

            else:
                print("Sorry, invalid input. You should enter only numbers.")
        else:
            print("Your list is empty")
    else:
        print("Exiting program... Good bye.")