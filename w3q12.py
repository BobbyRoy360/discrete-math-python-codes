def is_harshad(n):
    if n <= 0:
        return False
    
    digits_sum = 0
    for char in str(n):
        digits_sum += int(char)
    
    if n % digits_sum == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_harshad(number):
    print(number, "is a Harshad number")
else:
    print(number, "is not a Harshad number")