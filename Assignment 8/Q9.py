# Function to check if number is palindrome

def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return original == rev

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")