import time

def is_pronic(n):
    if n < 0:
        return False
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i = i + 1
    return False

num = int(input("Enter a number: "))

start = time.time()
result = is_pronic(num)
end = time.time()

if result:
    print("True")
else:
    print("False")

print("Run time:", end - start)