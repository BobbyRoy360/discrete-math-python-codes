import time

def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    exponent = (p - 1) // 2
    val = pow(a, exponent, p)
    if val == p - 1:
        return -1
    return val

try:
    a = int(input("Enter integer a: "))
    p = int(input("Enter odd prime p: "))

    start_time = time.time()
    result = legendre_symbol(a, p)
    end_time = time.time()

    print("Legendre Symbol:", result)
    print("Time taken:", end_time - start_time, "seconds")

except ValueError:
    print("Please enter valid integers")