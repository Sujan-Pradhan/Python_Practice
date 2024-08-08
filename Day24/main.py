# file = open("my_file.txt")
# contents = file.read()
# print (contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print (contents)

# with open("my_file.txt",mode="a") as file:
#     contents = file.write("\nI am 23 years old.\nI like to play football.\n")

with open('new_file.txt',mode='w') as new_file:
    new_file.write("New text file.")