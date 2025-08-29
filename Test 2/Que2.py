# Program to check condition on 3-digit number

num = int(input("Enter a 3 digit number"))

first = num // 100 
second = (num // 10) % 10
third = num % 10

if first == 2 * second and first == third / 2:
    print("yes, you have done it")
else:
    print("please try next time")