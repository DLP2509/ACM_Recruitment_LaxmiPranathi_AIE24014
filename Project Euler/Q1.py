sum = 0
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("The sum of all multiples of 3 and 5 below 100 is:", sum)
