for i in range(5):
    for j in range(6):
        
        if i == 0 or i == 5 - 1 or j == 0 or j == 6 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
            