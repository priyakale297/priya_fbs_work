def print_patterns(n):
    print('*' * n)
    
    for i in range(1, n - 9):
        print('  ' * (i -1) + '*')
    
    print('*' * n )

n = 20
print_patterns(n)