# def create_file (file_name):
#     file = open(file_name, 'w', encoding="utf-8")
#     file.close()
#
# def read_the_file (file_name):
#     file = open(file_name, 'r', encoding="utf-8")
#     for line in file:
#         print(line)
#     file.close()

# file_name = input("Enter file name: ")
# create_file(file_name)

import re

def remove_tags (file_name):
    file = open(file_name, 'r', encoding="utf-8")
    for line in file:
        newline = re.findall(r">(.*)</", line)
        newline = str(newline).replace("]", "").replace("[", "").replace("'", "")
        if len(str(newline)) !=0:
            add_lines_to_file(file_name, newline)
    file.close()

def add_lines_to_file(file_name, newline):
    filename = str(file_name).replace(".html", "_new.html")
    file = open(filename, 'a', encoding="utf-8")
    file.write(newline)
    file.write("\n")
    file.close()


file_name = "index.html"
# read_the_file(file_name)

while True:
    massage = input("Would you like to remove all tags in index.html? (Type y/yes):\n").lower().strip()
    if massage == "yes" or massage == "y":
        remove_tags(file_name)
    else:
        print("Thank you for using this program. Goodbye!")
        break