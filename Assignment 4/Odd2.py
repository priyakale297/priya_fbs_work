#Program to print all Odd numbers until n

n = int(input('Enter a numbers:'))
print('Odd numbers up to',n,'are')
for i in range(1, n+1,2):
    print(i)