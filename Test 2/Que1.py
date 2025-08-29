# Program to check if a year is leap year or not
year = int(input("Enter a year:"))

if year % 4 == 0:          #1: check divisible by 4
    if year % 100 == 0:    #2: check divisible by 100
        if year % 400 == 0: #3: check divisoble by 400
            print(year, "is a Leap year")
        else:
            print(year, " is Not a Leap year")
    else:
        print(year, "is a Leap year")
else:
    print(year, "is Not a Leap year")