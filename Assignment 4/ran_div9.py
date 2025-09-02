# Program to print all numbers in a range divisible by a given number

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
divisor = int(input("Enter the number to divide by: "))

print(f"Numbers divisible by {divisor} in range {start} to {end} are:")
for i in range(start, end + 1):
    if i % divisor == 0:
        print(i, end=" ")