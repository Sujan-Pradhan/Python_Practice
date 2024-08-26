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

names = ["Sujan", "Sujata", "Susil", "Sujita","Susmita","Suhana"]

short_names= [name.upper() for name in names if len(name)>5]
print(short_names)
