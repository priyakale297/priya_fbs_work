n = int(input("Enter how many numbers you want: "))

numbers = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]

print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)
