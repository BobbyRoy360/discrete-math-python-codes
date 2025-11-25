import time

def mean_of_digits(n):
    digits = str(n)
    total = 0
    length = 0
    
    for d in digits:
        total = total + int(d)
        length = length + 1
        
    return total / length

num = int(input("Enter a number: "))

start_time = time.time()
result = mean_of_digits(num)
end_time = time.time()

print("Average of digits:", result)
print("Runtime:", end_time - start_time)