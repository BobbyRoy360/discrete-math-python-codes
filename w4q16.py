import time

def count_distinct_prime_factors(n):
    count = 0
    d = 2
    temp = n
    
    while d * d <= temp:
        if temp % d == 0:
            count = count + 1
            while temp % d == 0:
                temp = temp // d
        d = d + 1
    
    if temp > 1:
        count = count + 1
        
    return count

number = int(input("Enter a number: "))

start = time.time()
result = count_distinct_prime_factors(number)
end = time.time()

print("Number of distinct prime factors:", result)
print("Time taken:", end - start, "seconds")