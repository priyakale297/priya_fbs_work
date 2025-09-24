def print_factors(num):
    print(f"Factors of the given number {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=", ")

print_factors(12)