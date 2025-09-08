import math
n = int(input("Enter the value of n: "))

s = 0

for i in range(1, n+1):
    s += i /math.factorial(i)

print("Sum of the series is:", s)