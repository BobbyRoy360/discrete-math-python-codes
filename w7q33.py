import time

def collatz_length(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps = steps + 1
    return steps

number = int(input("Enter a number: "))

start = time.time()
result = collatz_length(number)
end = time.time()

print("Steps:", result)
print("Time taken:", end - start, "seconds")