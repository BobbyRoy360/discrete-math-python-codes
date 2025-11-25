import time
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    if n < 0:
        return False
    a = 0
    b = 1
    while a < n:
        temp = a
        a = b
        b = temp + b
    return a == n

def is_fibonacci_prime(n):
    if is_fibonacci(n) and is_prime(n):
        return True
    return False

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check: "))
        
        start_time = time.time()
        result = is_fibonacci_prime(num)
        end_time = time.time()
        
        if result:
            print(f"{num} is a Fibonacci Prime number.")
        else:
            print(f"{num} is NOT a Fibonacci Prime number.")
            
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        
    except ValueError:
        print("Please enter a valid integer.")