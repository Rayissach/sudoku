board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def sudoku_board(bo):

    for x in range(len(bo)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(bo[0])):
            if y % 3 == 0 and y != 0:
                print (" | ", end="")

            if y == 8:
                print(bo[x][y])
            else:
                print(str(bo[x][y]) + " ", end="")

sudoku_board(board)

def search_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo[0])):
            if bo[x][y] == 0:
                return(x, y) #row, col