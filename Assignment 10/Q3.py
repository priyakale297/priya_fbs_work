li = [10, 20, 4, 45, 99, 95, 70, 45]

largest = max(li)

while largest in li:
    li.remove(largest)
    
if li:
    second_largest = max(li)
    print("Second largest element is:", second_largest)
else:
    print("No second largest element found.")
