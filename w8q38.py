import time

def zeta_approx(s, terms):
    total = 0
    for i in range(1, terms + 1):
        total = total + (1 / (i ** s))
    return total

s_input = 2
n_terms = 100000

start = time.time()
result = zeta_approx(s_input, n_terms)
end = time.time()

print("Result:", result)
print("Time taken:", end - start, "seconds")