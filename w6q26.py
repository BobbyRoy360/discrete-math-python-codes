import time

def mod_inverse(a, m):
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return -1

try:
    a_val = int(input("Enter a: "))
    m_val = int(input("Enter m: "))

    start_time = time.time()
    result = mod_inverse(a_val, m_val)
    end_time = time.time()

    print("Modular Multiplicative Inverse is:", result)
    print("Time taken:", end_time - start_time, "seconds")

except ValueError:
    print("Please enter valid integers")