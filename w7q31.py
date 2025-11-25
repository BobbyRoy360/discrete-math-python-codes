import time

def lucas_sequence(n):
    lucas_list = []
    
    if n >= 1:
        lucas_list.append(2)
    if n >= 2:
        lucas_list.append(1)
        
    for i in range(2, n):
        next_num = lucas_list[i-1] + lucas_list[i-2]
        lucas_list.append(next_num)
        
    return lucas_list

n = int(input("Enter the number of terms: "))

start = time.time()
result = lucas_sequence(n)
end = time.time()

print("Lucas Sequence:", result)
print("Time taken:", end - start)