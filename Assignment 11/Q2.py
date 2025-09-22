li1 = [34, 12, 5, 66]
li2 = [3, 22, 90, 1]


merged_list = [0] * (len(li1) + len(li2))

i = 0
while i < len(li1):
    merged_list[i] = li1[i]
    i += 1

j = 0
while j < len(li2):
    merged_list[i] = li2[j]
    i += 1
    j += 1
n = len(merged_list)
x = 0
while x < n - 1:
    y = 0
    while y < n - x - 1:
        if merged_list[y] > merged_list[y + 1]:
        
            temp = merged_list[y]
            merged_list[y] = merged_list[y + 1]
            merged_list[y + 1] = temp
        y += 1
    x += 1

print("Merged and Sorted List:")
k = 0
while k < len(merged_list):
    print(merged_list[k], end=" ")
    k += 1
