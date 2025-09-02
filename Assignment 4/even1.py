#Program to print all even numbers until n

n = int(input('Enter a number:'))

print('Even numbers are to', n, 'are')
for i in range(2, n+1,2):
    print(i)