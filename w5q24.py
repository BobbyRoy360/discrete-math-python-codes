import time

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    return count

def is_highly_composite(n):
    n_divisors = count_divisors(n)
    
    for i in range(1, n):
        i_divisors = count_divisors(i)
        if i_divisors >= n_divisors:
            return False
            
    return True

num = int(input("Enter a number: "))

start = time.time()
result = is_highly_composite(num)
end = time.time()

print(result)
print("Run time:", end - start)