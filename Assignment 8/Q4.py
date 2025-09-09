# Function to calculate sum of odd numbers up to n

def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2):  
        total += i
    return total

n = int(input("Enter the value of n: "))
print("Sum of all odd numbers between 1 to", n, "=", sum_odd(n))