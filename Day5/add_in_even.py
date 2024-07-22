total_even = 0
for n in range(2,101,2):
    total_even += n
print(total_even)

total_even2 = 0
for number in range(1,101):
    if number %2 == 0:
        total_even2 += number  
print(total_even2)