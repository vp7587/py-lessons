def difference (*arg):
    arg_list = list(arg)
    if arg_list:
        min_value = min(arg_list)
        max_value = max(arg_list)
        result = round ((max_value - min_value), 2)
    else:
        result = 0
    return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')