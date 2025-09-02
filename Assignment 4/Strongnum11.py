# Program to check if a number is a Strong Number

num = int(input("Enter a number: "))
temp = num
sum_of_fact = 0

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

while temp > 0:
    digit = temp % 10
    sum_of_fact += factorial(digit)
    temp //= 10

if sum_of_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")