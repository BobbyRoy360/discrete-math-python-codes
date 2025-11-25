import time

def find_modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    
    if m == 1:
        return 0
        
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
        
    if x < 0:
        x = x + m0
        
    return x

def crt(remainders, moduli):
    total_product = 1
    for x in moduli:
        total_product = total_product * x
        
    result = 0
    for i in range(len(moduli)):
        current_mod = moduli[i]
        current_remainder = remainders[i]
        
        partial_product = total_product // current_mod
        inverse = find_modular_inverse(partial_product, current_mod)
        
        result = result + (current_remainder * partial_product * inverse)
        
    return result % total_product

if __name__ == "__main__":
    a = [2, 3, 2]
    m = [3, 5, 7]
    
    start_time = time.time()
    
    solution = crt(a, m)
    
    end_time = time.time()
    
    print("System of congruences:")
    for i in range(len(a)):
        print("x =", a[i], "mod", m[i])
        
    print("\nSolution x =", solution)
    print("Runtime:", end_time - start_time, "seconds")