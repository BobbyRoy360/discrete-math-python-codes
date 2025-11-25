import time

def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        
        start_time = time.time()
        result = multiplicative_persistence(num)
        end_time = time.time()
        
        print(f"Multiplicative Persistence: {result}")
        print(f"Run time: {end_time - start_time} seconds")
        
    except ValueError:
        print("Please enter a valid integer")