import time
import math

def order_mod(a, n):
    if math.gcd(a, n) != 1:
        return -1
    
    k = 1
    current = a % n
    
    while current != 1:
        current = (current * a) % n
        k += 1
        
    return k

a = 3
n = 7

start_time = time.time()
result = order_mod(a, n)
end_time = time.time()

print(f"The order is: {result}")
print(f"Run time: {end_time - start_time} seconds")