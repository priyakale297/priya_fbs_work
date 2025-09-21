li = [12, 7, 9, 12, 15, 12, 20, 7, 12]

num = int(input("Enter a number to check in the list: "))

if num in li:
    count = li.count(num)
    print(f"{num} is present in the list.")
    print(f"It appears {count} time(s).")
else:
    print(f"{num} is not present in the list.")
