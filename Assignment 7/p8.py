for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("    " * (5 - i), end= " ")
    
    for j in range(i, 0, -1):
        print(j, end=" " )

    print()