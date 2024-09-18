import math
smallest_number = 1
for i in range(1, 21):
    gcd = math.gcd(smallest_number, i)
    lcm = (smallest_number * i) // gcd
    smallest_number = lcm
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", smallest_number)
