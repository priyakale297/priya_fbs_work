def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter the value of n: "))

print("a) Sum of 1 + 2 + ... + n =", sum_natural(n))
print("b) Sum of 1! + 2! + ... + n! =", sum_factorial(n))
print("c) Sum of 1^1 + 2^2 + ... + n^n =", sum_power(n))