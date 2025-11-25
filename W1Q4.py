import math

def prime_pi(n: int) -> int:
    
    
   
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    
    if n < 2:
        return 0
    
    
    is_prime = [True] * (n + 1)
    
   
    is_prime[0] = is_prime[1] = False
    
    
    limit = int(math.sqrt(n))
    
    
    for p in range(2, limit + 1):
        
        if is_prime[p]:
            
            for j in range(p * p, n + 1, p):
                is_prime[j] = False
                
    
    return sum(is_prime)


print(f"π(10) = {prime_pi(10)}")  # Expected: 4
print(f"π(100) = {prime_pi(100)}") # Expected: 25