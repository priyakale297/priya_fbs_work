# Program to find minimum number of notes for a given amount

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum notes required:")

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} x {count}")