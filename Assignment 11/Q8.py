board = [[0] * 10 for _ in range(10)]  

num = 1
row = 9  
while row >= 0:
    col = 0

    if (9 - row) % 2 == 0:
        while col < 10:
            board[row][col] = num
            num += 1
            col += 1
    else:
        col = 9
        while col >= 0:
            board[row][col] = num
            num += 1
            col -= 1

    row -= 1

r = 0
while r < 10:
    c = 0
    while c < 10:
        print(board[r][c], end="\t")
        c += 1
    print()  
    r += 1
