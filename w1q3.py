import time

def divisor_sum(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

try:
    number = int(input("Enter a number: "))
    
    start_time = time.time()
    result = divisor_sum(number)
    end_time = time.time()
    
    print(f"The sum of divisors of {number} is: {result}")
    print(f"Time taken: {end_time - start_time} seconds")
    
except ValueError:
    print("Please enter a valid integer")