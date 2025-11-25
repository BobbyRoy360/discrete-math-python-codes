import time

def is_quadratic_residue(a, p):
    for x in range(p):
        if (x * x) % p == a:
            return True
    return False

if __name__ == "__main__":
    a = 2
    p = 7
    
    start = time.time()
    result = is_quadratic_residue(a, p)
    end = time.time()
    
    print(result)
    print(f"Time taken: {end - start} seconds")