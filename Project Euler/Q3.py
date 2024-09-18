number = 600851475143
largest_factor = 1
while number % 2 == 0:
    largest_factor = 2
    number = number // 2
i = 3
while i * i <= number:
    if number % i == 0:
        largest_factor = i
        while number % i == 0:
            number = number // i
    i += 2
if number > 2:
    largest_factor = number
print("The largest prime factor of 600851475143 is:", largest_factor)
