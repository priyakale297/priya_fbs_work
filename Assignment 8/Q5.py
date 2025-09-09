# Function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    total = 0
    for i in range(2, n + 1):
        if is_prime(i):
            total += i
    return total

n = int(input("Enter the value of n: "))
print("Sum of all prime numbers between 1 to", n, "=", sum_primes(n))