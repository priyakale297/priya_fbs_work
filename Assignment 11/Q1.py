li = [12, 7, 9, 14, 5, 20, 3, 18]

even_list = [0] * len(li)
odd_list = [0] * len(li)

even_index = 0
odd_index = 0

i = 0
while i < len(li):
    num = li[i]
    
    if num % 2 == 0:
        even_list[even_index] = num
        even_index += 1
    else:
        odd_list[odd_index] = num
        odd_index += 1
    i += 1
print("Original List:", li)

print("Even elements:", end=" ")
j = 0
while j < even_index:
    print(even_list[j], end=" ")
    j += 1

print("\nOdd elements:", end=" ")
k = 0
while k < odd_index:
    print(odd_list[k], end=" ")
    k += 1
