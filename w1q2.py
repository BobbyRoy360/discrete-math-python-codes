import time

def mobius(n):
    if n == 1:
        return 1
    
    factors = 0
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            factors += 1
            n //= i
            if n % i == 0:
                return 0
        else:
            i += 1
            
    if n > 1:
        factors += 1
        
    if factors % 2 == 0:
        return 1
    else:
        return -1

try:
    num = int(input("Enter a positive integer: "))
    
    start_time = time.time()
    result = mobius(num)
    end_time = time.time()
    
    print("Mobius value:", result)
    print("Time taken:", end_time - start_time, "seconds")
    
except ValueError:
    print("Please enter a valid integer")