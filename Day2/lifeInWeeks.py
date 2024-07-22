age = int(input("What is your current age?"))

years_remaining = int(90-age)
days = years_remaining * 365
weeks = years_remaining * 52
# weeks = round(days / 7,2)
months = years_remaining * 12
# months = round(days/30,2)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")