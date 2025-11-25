def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

number = int(input("Enter a number: "))
print(is_palindrome(number))