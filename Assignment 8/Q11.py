# Function to count digits

def count_digits(num):
    return len(str(num))

def is_armstrong(num):
    n = count_digits(num)
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10
    return sum_of_powers == num

def main():
    number = int(input("Enter a number: "))
    if is_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

main()