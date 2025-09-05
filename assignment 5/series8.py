# a. Sum of factorial series
import math

n = int(input("Enter value of n: "))
total = 0

for i in range(1, n+1):
    total += math.factorial(i)

print("Sum of factorial series =", total)

# b. Power series
N = int(input("Enter value of N: "))
total = 0

for i in range(1, N+1):
    total += N**i

print("Sum of power series =", total)

# c. Geometric series with ratio 2
n = int(input("Enter number of terms: "))
total = 0

for i in range(n):
    total += 2**i   # since ratio = 2, first term = 1

print("Sum of geometric series =", total)

# d. Series with division
a = int(input("Enter value of a: "))
S = 0

for i in range(1, 11):
    S += (a**i) / i

print("Sum of series =", S)

# e. Alternating series
x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

S = 0
sign = 1
denominator = 1

for i in range(1, n+1):
    term = (x**i) / denominator
    S += sign * term
    sign *= -1        # alternate sign
    denominator += 2  # 1, 3, 5, 7...

print("Sum of alternating series =", S)