import time

def is_prime_power(n):
    if n <= 1:
        return False
    
    p = 0
    for i in range(2, n + 1):
        if n % i == 0:
            p = i
            break
            
    while n > 1:
        if n % p != 0:
            return False
        n = n // p
        
    return True

start_time = time.time()

print(is_prime_power(27))
print(is_prime_power(10))
print(is_prime_power(13))
print(is_prime_power(32))

end_time = time.time()
print("Run time:", end_time - start_time)