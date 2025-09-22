li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]
n1 = 0
for _ in li1:
    n1 += 1

n2 = 0
for _ in li2:
    n2 += 1

union = [0] * (n1 + n2)

i = 0
while i < n1:
    union[i] = li1[i]
    i += 1
k = i 
j = 0
while j < n2:
    found = False
    m = 0
    while m < k:
        if union[m] == li2[j]:
            found = True
        m += 1
    if not found:
        union[k] = li2[j]
        k += 1
    j += 1

print("Union of the two lists:")
x = 0
while x < k:
    print(union[x], end=" ")
    x += 1
