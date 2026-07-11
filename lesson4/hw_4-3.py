import random
print("The raw range with random elements quantity from 3 to 10 will be created \n"
      "Using the raw range the final list will be formed \n"
      "The final list should consists 1, 3 and the 2 from the range end\n")
random_range_len = (random.randint(3, 10))
print(f"Random raw range len: {random_range_len}")
raw_range = list(range(random_range_len))
print(f"Random raw range: {raw_range}")
final_list = []
final_list.append(raw_range[0])
final_list.append(raw_range[2])
final_list.append(raw_range[-2])
print(f"Final list: {final_list}")


