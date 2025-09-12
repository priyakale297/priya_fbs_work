def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

def sum_of_series(n):
    if n == 1:
        return fact(1)
    else:
        return fact(n) + sum_of_series(n - 1)

n = int(input("Enter the value of n: "))
result = sum_of_series(n)
print("Sum of the series 1! + 2! + ... +", n, "! =",result)