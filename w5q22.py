import time

def sum_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total

def are_amicable(a, b):
    sum_a = sum_divisors(a)
    sum_b = sum_divisors(b)
    
    if sum_a == b and sum_b == a:
        return True
    else:
        return False

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

start_time = time.time()

result = are_amicable(num1, num2)

end_time = time.time()

if result:
    print("The numbers are amicable")
else:
    print("The numbers are not amicable")

print("Time taken:", end_time - start_time, "seconds")