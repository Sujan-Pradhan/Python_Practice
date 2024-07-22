print("Welcome to the BMI Calculator!!")

height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

BMI = round(weight/height**2,2)

if(BMI<18.5):
    print(f"Your BMI is {BMI}, you are underweight.")
elif(BMI>18.5 and BMI<25):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif(BMI>25 and BMI<30):
    print(f"Your BMI is {BMI}, you have overweight.")
elif(BMI>30 and BMI<35):
    print(f"Your BMI is {BMI}, you have obese.")
else:
    print(f"Your BMI is {BMI}, you clinically obese.")