import time

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

n = int(input("Enter a number: "))

start = time.time()
result = count_divisors(n)
end = time.time()

print(f"Number of divisors: {result}")
print(f"Time taken: {end - start} seconds")