import time

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))

start = time.time()
result = prime_factors(number)
end = time.time()

print(result)
print("Time taken:", end - start)