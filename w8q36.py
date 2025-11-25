import random
import time

def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        is_composite = True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                is_composite = False
                break
        
        if is_composite:
            return False

    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter number to test: "))
        rounds = int(input("Enter number of rounds (k): "))
        
        start_time = time.time()
        result = is_prime_miller_rabin(num, rounds)
        end_time = time.time()
        
        print("Result:", result)
        print("Time taken:", end_time - start_time, "seconds")
        
    except ValueError:
        print("Please enter valid integers")