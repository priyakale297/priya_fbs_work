for i in range(1, 5 + 1):
    for j in range(5 - i):
        print('  ' , end = ' ')
    
    for j in range(2 * i - 1):
        print('*' , end = '  ')
    print()