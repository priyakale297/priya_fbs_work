li = [[1, 4], [3, 1], [5, 2], [7, 0]]
n = len(li)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if li[j][1] > li[j + 1][1]:
        
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp
        j += 1
    i += 1

print("Sorted list based on second element in each sublist:")
k = 0
while k < len(li):
    print(li[k])
    k += 1
