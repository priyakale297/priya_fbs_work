li = [12, 45, 23, 67, 34]
n = len(li)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if li[j] < li[j + 1]: 
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp
        j += 1
    i += 1
second_largest = li[1]

print("Sorted List (Descending):")
k = 0
while k < len(li):
    print(li[k], end=" ")
    k += 1

print("\nSecond Largest Number:", second_largest)
