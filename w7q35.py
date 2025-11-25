import math
import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_carmichael(n):
    if is_prime(n):
        return False
    
    for a in range(2, n):
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True

number_to_check = int(input("Enter a number: "))

start_time = time.time()
result = is_carmichael(number_to_check)
end_time = time.time()

print(f"Is {number_to_check} a Carmichael number? {result}")
print(f"Time taken: {end_time - start_time} seconds")