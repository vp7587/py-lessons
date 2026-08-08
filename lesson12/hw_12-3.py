import re

def is_even(number):
    even_list = [2,4,6,8]
    last_number = re.search(r'.$', str(number))
    last_number = last_number.group()
    if int(last_number) in even_list:
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
