import time

def is_perfect_power(n):
    if n <= 1:
        return True
    
    limit = int(n ** 0.5)
    
    for a in range(2, limit + 1):
        temp = a * a
        while temp <= n:
            if temp == n:
                return True
            temp = temp * a
            
    return False

n = int(input("Enter a number: "))

start = time.time()
result = is_perfect_power(n)
end = time.time()

print(result)
print(end - start)
