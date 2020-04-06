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

def solve_board(brd):

    find = search_empty(brd)
    if not find:
        return True 
    else:
        row, col = find

    for x in range(1,10):
        if valid(brd, x, (row, col)):
            brd[row][col] = x

            if solve_board(brd):
                return True

            brd[row][col] = 0

    return False

def valid(brd, num, pos):

    #Check row
    for x in range(len(brd[0])):
        if brd[pos[0]][x] == num and pos[1] != x:
            return False
    
    #Check column
    for x in range(len(brd)):
        if brd[x][pos[1]] == num and pos[0] != 1:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for x in range(box_y*3, box_y*3 +3):
        for y in range(box_x*3, box_x*3 + 3):
            if brd[x][y] == num and (x,y) != pos:
                return False 

def sudoku_board(brd):

    for x in range(len(brd)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(brd[0])):
            if y % 3 == 0 and y != 0:
                print (" | ", end="")

            if y == 8:
                print(brd[x][y])
            else:
                print(str(brd[x][y]) + " ", end="")


def search_empty(brd):
    for x in range(len(brd)):
        for y in range(len(brd[0])):
            if brd[x][y] == 0:
                return(x, y) #row, col

    return None 

sudoku_board(board)
solve_board(board)
print("_____________________")
sudoku_board(board)