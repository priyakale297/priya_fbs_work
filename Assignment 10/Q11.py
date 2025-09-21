li = [10, 15, 20, 30, 40, 45, 60, 75, 90]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

divisible_by_both = [num for num in li if num % m == 0 and num % n == 0]

print(f"Numbers divisible by both {m} and {n}:", divisible_by_both)
