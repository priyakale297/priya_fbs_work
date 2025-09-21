n = int(input("Enter the number of elements: "))

original_li = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    original_li.append(element)

even_li = [num for num in original_li if num % 2 == 0]
odd_li = [num for num in original_li if num % 2 != 0]

print("Original List:", original_li)
print("Even Elements List:", even_li)
print("Odd Elements List:", odd_li)
