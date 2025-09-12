def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))

if num < 0:
    reversed_num = -reverse_number(-num)
else:
    reversed_num = reverse_number(num)

print("Reversed number:", reversed_num)