li = 10

numbers = [0] * li
squares = [0] * li
cubes = [0] * li
i = 0
num = 1
while i < li:
    numbers[i] = num
    squares[i] = num * num
    cubes[i] = num * num * num
    i += 1
    num += 1

print("Number\tSquare\tCube")
j = 0
while j < li:
    print(numbers[j], "\t", squares[j], "\t", cubes[j])
    j += 1
