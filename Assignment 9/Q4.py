def sum_recursive(numbers, n):
    if n == 0:
        return 0
    else:
        return numbers[n - 1] + sum_recursive(numbers, n - 1)

n = int(input("Enter how many numbers: "))
numbers = []

print("Enter the numbers:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

result = sum_recursive(numbers, n)
print("Sum of the numbers is:", result)