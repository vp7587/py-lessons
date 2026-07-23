import sys,string

print("The program includes function, which finds second inclusion of substring in text")

def second_index(text, sub_str) -> int|None:
  index = text.find(sub_str)
  result = text.find(sub_str, index+1)
  if result == -1:
      result = None
  return result

while True:
    run_program = str.strip(str.lower(input("\nWould you like to continue?(Type y/yes if you do):\n")))
    if run_program == "y" or run_program == "yes":
        assert second_index("sims", "s") == 3, 'Test1'
        assert second_index("find the river", "e") == 12, 'Test2'
        assert second_index("hi", "h") is None, 'Test3'
        assert second_index("Hello, hello", "lo") == 10, 'Test4'
        print('Test ОК')
    else:
        print("Good bye.")
        sys.exit()

