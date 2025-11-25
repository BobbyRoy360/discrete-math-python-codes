def is_abundant(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    
    if total > n:
        return True
    else:
        return False

number = 12
result = is_abundant(number)
print(f"Is {number} abundant? {result}")

number = 10
result = is_abundant(number)
print(f"Is {number} abundant? {result}")