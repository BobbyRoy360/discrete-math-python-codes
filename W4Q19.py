import time

def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True

def twin_primes(limit):
    pairs = []
    n = 2
    while n + 2 <= limit:
        if is_prime(n):
            if is_prime(n + 2):
                pair = (n, n + 2)
                pairs.append(pair)
        n = n + 1
    return pairs

start_time = time.time()
result = twin_primes(2000)
end_time = time.time()

print(result)

elapsed_time = end_time - start_time
print("Runtime:")
print(elapsed_time)