def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)
base = int(input("Enter the base (m): "))
exponent = int(input("Enter the exponent (n): "))

result = power(base, exponent)
print(f"{base} to the power {exponent} is: {result}")