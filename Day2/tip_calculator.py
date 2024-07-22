print("Welcome to the tip calculator.")
total_bill  = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_given_by_each_person = round(((1+(tip_percentage/100))*total_bill)/number_of_people,2)

print(f"Each person should pay: ${tip_given_by_each_person}")