year = int(input("Which year do you want to check? "))
# if(year%4==0):
#     print(f"So the year {year} is a leap year")
# elif(year%100==0 and year%400==0):
#     print(f"So the year {year} is a leap year")
# else:
#     print(f"The given year {year} is not a leap year")


if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")