#Програма ищет не только нули. Пользователь сам в начале вводит число, которое зотел бы переместить и массив,
# в котором эточисло искать. Так Более универсально и интересно
print("The program will move all numbers you'll enter next step from the list to the end of the list.\n")
run = "y"
while run == "y" or run == "Y"  or run == "YES" or run == "yes":
    run = str.lower(input("Would you like to continue?(Type y/yes if you do):\n"))
    if run == "y" or run == "yes":
        user_value_to_move = (input("Please, enter number you want to move: \n"))
        if user_value_to_move.isdigit():
            print("You should input a few numbers as string, including number you want to move.\n")
            raw_text= input("Please enter a few numbers like this: 0123456\n")
            if raw_text:
                if raw_text.isdigit():
                    numbers_list = list(raw_text)
                    count_numbers_list_elements = len(numbers_list)
                    print(f"Your list is not empty. Ok. Going ahead..")
                    if count_numbers_list_elements == 1:
                        print(f"Your has only one item")
                    else:
                        user_value_to_move_in_list =  numbers_list.count(user_value_to_move)
                        if user_value_to_move_in_list == 0:
                            print(f"Sorry, your list has no your number.")
                        else:
                            print(f"Well, your list has {user_value_to_move_in_list} your numbers. Going ahead..")
                            i = 0
                            #Непосредственно перемещение элементов
                            while i < user_value_to_move_in_list:
                                index_of_user_value_to_move_in_list = numbers_list.index(user_value_to_move)
                                numbers_list.remove(user_value_to_move)
                                numbers_list.append(user_value_to_move)
                                i += 1
                            print(f"The final list is: {numbers_list}")
                else:
                    print("Sorry, invalid input. You should enter only numbers.")
            else:
                print("Your list is empty")
        else:
            print("Sorry, invalid input. You should enter only numbers.")
    else:
        print("Exiting program... Good bye.")