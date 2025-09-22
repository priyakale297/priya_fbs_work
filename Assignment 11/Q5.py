li = ["banana", "kiwi", "apple", "mango", "cherry"]
def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

n = 0
for _ in li:
    n += 1

i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if get_length(li[j]) > get_length(li[j + 1]):
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp
        j += 1
    i += 1
print("Sorted List by Element Length:")
k = 0
while k < n:
    print(li[k])
    k += 1
