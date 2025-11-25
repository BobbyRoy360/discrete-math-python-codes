import time

def polygonal_number(s, n):
    part1 = (s - 2) * n * n
    part2 = (s - 4) * n
    result = (part1 - part2) // 2
    return result

s_input = int(input("Enter the value of s (sides): "))
n_input = int(input("Enter the value of n (position): "))

start_time = time.time()
answer = polygonal_number(s_input, n_input)
end_time = time.time()

print("The polygonal number is:")
print(answer)
print("Time taken to run:")
print(end_time - start_time)