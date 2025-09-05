# Program to calculate percentage of students and average percentage


n = int(input("Enter number of students: "))

percentages = []  # list to store each student's percentage

for i in range(1, n+1):
    print(f"\nEnter marks for Student {i}:")
    total = 0
    for j in range(1, 6):  # 5 subjects
        marks = int(input(f"  Enter marks of subject {j}: "))
        total += marks
    percentage = total / 5  # since 5 subjects
    percentages.append(percentage)

for i in range(n):
    print(f"Student {i+1}: {percentages[i]:.2f}%")

avg_percentage = sum(percentages) / n
print(f"\nAverage Percentage of class: {avg_percentage:.2f}%")