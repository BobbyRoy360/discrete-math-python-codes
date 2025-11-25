import time

def partition_function(n):
    start_time = time.time()
    
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ways[j] += ways[j - i]
            
    end_time = time.time()
    print("Time taken:", end_time - start_time)
    
    return ways[n]

number = int(input("Enter a number: "))
result = partition_function(number)
print("Distinct ways:", result)