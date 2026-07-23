import sys

print("The program generates two ranges.\n"
      "User puts a len of ranges between 1 and 100, and a step number for both lists.\n"
      "The result should be a set of common elements.\n")

def common_elements(set_1, set_2):
        set_1 = set(set_1)
        set_2 = set(set_2)
        result = f"common elements set is: {set_1.intersection(set_2)}"
        if len(result) == 0:
            result = "No common elements found"
        return result

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        range_length = input("Enter the range length: ").strip()
        if not range_length.isdigit():
            print("Error: the range length should be a number. Try again")
            continue
        range_length = int(range_length)
        if not 0 < range_length <= 100:
            print("Error: the range length should be between 1 and 100. Try again")
            continue
        step_1 = (input("Enter the first step: ")).strip()
        if not step_1.isdigit():
            print("Error: the step should be a number. Try again")
            continue
        step_2 = (input("Enter the second step: ")).strip()
        if not step_2.isdigit():
            print("Error: the step should be a number. Try again")
            continue
        first_list = list(range(1, range_length,int(step_1)))
        print(f"The first list is: {first_list}\n")
        second_list = list(range(1, range_length,int(step_2)))
        print(f"The second list is: {second_list}\n")
        print(f"Result: {common_elements(first_list,second_list)}")
    else:
        print("Good bye.")
        sys.exit()