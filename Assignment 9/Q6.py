def sum_of_digits(n):
    if n == 0:
        return 0  
    else:
        return n % 10 + sum_of_digits(n // 10)
    
num = int(input("Enter a number: "))

num = abs(num)

result = sum_of_digits(num)
print("Sum of digits:", result)