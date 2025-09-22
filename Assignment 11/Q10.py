li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 0
for _ in li:
    n += 1
result = [0] * n
k = 0  
i = 0
while i < n:
    if li[i] % 2 != 0: 
        result[k] = li[i]
        k += 1
    i += 1

print("List after removing even numbers:")
j = 0
while j < k:
    print(result[j], end=" ")
    j += 1
