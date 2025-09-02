#Program to find the sum of series upto n

n = int(input('Entera number:'))
total = 0
for i in range(1,n +1):
    total +=i
print('sum of series upto', n,'=', total)