import time

def is_automorphic(n):
    sq = n * n
    original = str(n)
    square = str(sq)
    
    if square.endswith(original):
        return True
    else:
        return False

num = int(input("Enter a number to check: "))

start = time.time()
result = is_automorphic(num)
end = time.time()

if result:
    print(num, "is an automorphic number")
else:
    print(num, "is not an automorphic number")

print("Run time:", end - start)