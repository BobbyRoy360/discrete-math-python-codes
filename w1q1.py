import math
import time

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_phi(n):
    count = 0
    for k in range(1, n + 1):
        if get_gcd(n, k) == 1:
            count += 1
    return count

def euler_phi_efficient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result - (result // p)
        p += 1
    if n > 1:
        result = result - (result // n)
    return result

if __name__ == "__main__":
    number = 10000 
    
    print(f"Calculating phi({number})...")
    
    start_time = time.time()
    answer = euler_phi(number)
    end_time = time.time()
    
    print(f"Result (Counting Method): {answer}")
    print(f"Time Taken: {end_time - start_time:.5f} seconds")
    print("-" * 30)

    start_time = time.time()
    answer_fast = euler_phi_efficient(number)
    end_time = time.time()
    
    print(f"Result (Efficient Method): {answer_fast}")
    print(f"Time Taken: {end_time - start_time:.5f} seconds")