print("You should input a few numbers as string.\n"
      "The program will divine string into 2 sublists and print one list of two sublists.\n")
raw_text= input("Please enter a few numbers like this: 123456\n")
if raw_text:
    if raw_text.isdigit():
        numbers_list = list(raw_text)
        count_numbers_list_elements = len(numbers_list)
        print(f"Your list consists of {count_numbers_list_elements}")
        if count_numbers_list_elements == 1:
            print(f"The final list of 2 sublists is: [[{numbers_list}],[]]")
        else:
            middle_index = count_numbers_list_elements // 2
            print(f"The middle element is: {numbers_list[middle_index]}")
            if len(numbers_list) % 2 != 0:
                middle_index += 1
            part1 = numbers_list[:middle_index]
            print(f"The first sublist is: {part1}")
            part2 = numbers_list[middle_index:]
            print(f"The second sublist is: {part2}")
            result = [part1, part2]
            print(f"The final list of 2 sublists is: {result}")
    else:
        print("Sorry, invalid input. You should enter only numbers.")
else:
    print("Your list is empty, result is: [[],[]]")