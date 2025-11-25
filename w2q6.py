import time

def factorial(n):
    if n < 0:
        return "Error: Number must be non-negative"
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

try:
    num = int(input("Enter a non-negative integer: "))
    
    start_time = time.time()
    answer = factorial(num)
    end_time = time.time()
    
    print("The factorial of", num, "is", answer)
    print("Time taken:", end_time - start_time, "seconds")

except ValueError:
    print("Please enter a valid integer")