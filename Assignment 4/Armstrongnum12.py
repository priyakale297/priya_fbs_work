# Program to print Armstrong numbers within a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    order = len(str(num))
    
    temp = num
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    
    if sum_of_powers == num:
        print(num, end=" ")