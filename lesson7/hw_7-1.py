import sys
print("The program shows greeting message, according given name and age.")
def say_hello(var_name, var_age) -> str:
    result = f"Hello. My name is {var_name} and I'm {var_age} years old"
    return result

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        name = input("\nWhat is your name?\n").strip()
        age = input("\nWhat is your age?\n").strip()
        assert say_hello(name, age) == f"Hello. My name is {name} and I'm {age} years old", 'check name and age'
        print(say_hello(name, age))
    else:
        print("Good bye.")
        sys.exit()