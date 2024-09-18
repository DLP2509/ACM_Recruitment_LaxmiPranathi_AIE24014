def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 :
            return False
        i += 2
    return True
prime_count = 0
current_number = 1
required_prime_number = 10001

while prime_count < required_prime_number:
    current_number += 1
    if prime(current_number):
        prime_count += 1

print("The 10001st prime number is: ",current_number)
