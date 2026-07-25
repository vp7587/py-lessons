import sys
print("The program makes int from list, adds 1 and returns list from int")

def add_one(some_list):
    number = ""
    for i in some_list:
        number = number+str(i)
    number = int(number)+1
    number_list = []
    for i in str(number):
        number_list.append(int(i))
    return number_list

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
        assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
        assert add_one([0]) == [1], 'Test3'
        assert add_one([9]) == [1, 0], 'Test4'
        print("ОК")
    else:
        print("Good bye.")
        sys.exit()