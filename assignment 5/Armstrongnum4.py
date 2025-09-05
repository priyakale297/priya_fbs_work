# Program to check if a number is Armstrong or not

num = int(input("Enter a number: "))

num_str = str(num)
power = len(num_str)

armstrong_sum = 0
for digit in num_str:
    armstrong_sum += int(digit) ** power

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")