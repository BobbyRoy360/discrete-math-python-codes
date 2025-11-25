import time

def digital_root(n):
    
    
    
    while len(str(n)) > 1:
        
        
        new_sum = 0
        
        
        number_as_string = str(n)
        
        
        for digit_char in number_as_string:
            
            new_sum = new_sum + int(digit_char)
            
        
        n = new_sum
        
    
    return n


number1 = 493193
start_time1 = time.time() 
result1 = digital_root(number1)
end_time1 = time.time()   

runtime1 = end_time1 - start_time1 
print(f"The digital root of {number1} is: {result1}")
print(f"Runtime for {number1}: {runtime1:.6f} seconds") 

print("-" * 30)


number2 = 942
start_time2 = time.time() 
result2 = digital_root(number2)
end_time2 = time.time()   

runtime2 = end_time2 - start_time2 
print(f"The digital root of {number2} is: {result2}")
print(f"Runtime for {number2}: {runtime2:.6f} seconds")