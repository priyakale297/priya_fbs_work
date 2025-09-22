li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]

n1 = 0
for _ in li1:
    n1 += 1

n2 = 0
for _ in li2:
    n2 += 1

intersection = [0] * (n1 if n1 < n2 else n2)
k = 0  

i = 0
while i < n1:
    j = 0
    while j < n2:
        if li1[i] == li2[j]:
        
            already_exists = False
            m = 0
            while m < k:
                if intersection[m] == li1[i]:
                    already_exists = True
                m += 1
            if not already_exists:
                intersection[k] = li1[i]
                k += 1
        j += 1
    i += 1

print("Intersection of the two lists:")
x = 0
while x < k:
    print(intersection[x], end=" ")
    x += 1
