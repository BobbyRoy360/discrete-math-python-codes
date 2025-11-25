import time

def is_deficient(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    
    if total < n:
        return True
    else:
        return False

n = int(input("Enter a number: "))

start_time = time.time()
result = is_deficient(n)
end_time = time.time()

print("Is the number deficient?", result)
print("Time taken:", end_time - start_time)