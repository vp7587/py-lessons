import sys

print("The program finds unique numbers in list")

def find_unique_value(some_list):
    uniq_values = []
    nonunique_values = []
    for i in some_list:
        if i not in uniq_values :
            uniq_values.append(i)
        else:
            nonunique_values.append(i)
    for i in nonunique_values:
        if i in uniq_values:
            uniq_values.remove(i)
    return uniq_values[0]

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
        assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
        assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
        print("\nAll tests are done.")
    else:
        print("Good bye.")
        sys.exit()