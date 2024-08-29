# ******  List Comprehension ******

# new_list = [new_item for item in list]


# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(new_list)


# name = "Sujan"
# new_list = [letter for letter in name]
# print(type(new_list))
# print(new_list)

# doubled_number = [n*2 for n in range(1,5)]
# print(doubled_number)


# *********** Conditional List Comprehension ****************
# new_list = [new_item for item in list if test]

# names = ["Sujan", "Sujata", "Susil", "Sujita","Susmita","Suhana"]

# short_names= [name.upper() for name in names if len(name)>5]
# print(short_names)


# Practice
# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [number*number for number in numbers]
# print(squared_numbers)

# even_numbers = [num for num in numbers if num%2==0]
# print(even_numbers)


with open ("file1.txt") as file1:
    file1 = file1.readlines()
    # print(file1)
with open ("file2.txt") as file2:
    file2 = file2.readlines()
    # print(file2)

result = [int(number) for number in file1 if number in file2]
print(result)