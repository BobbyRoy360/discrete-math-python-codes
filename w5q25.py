import time

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

if __name__ == "__main__":
    b = int(input("Enter base: "))
    e = int(input("Enter exponent: "))
    m = int(input("Enter modulus: "))

    start_time = time.time()
    ans = mod_exp(b, e, m)
    end_time = time.time()

    print("Result:", ans)
    print("Time taken:", end_time - start_time, "seconds")