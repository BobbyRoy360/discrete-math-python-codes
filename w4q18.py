import time
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    mersenne_number = 2 ** p - 1
    if is_prime(mersenne_number):
        print(f"2^{p} - 1 is a Mersenne Prime")
        return True
    else:
        print(f"2^{p} - 1 is NOT a Mersenne Prime")
        return False

p = 17

start_time = time.time()
is_mersenne_prime(p)
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")