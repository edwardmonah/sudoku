import pprint



def solve(bo):
    find = find_emp(bo)
    if find:
        row, col=find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col]=i

            if solve(bo):
                return True

            bo[row][col]=0

    return False

def valid(bo, pos, num):
    #returns if attempt is valid
    for i in range(0, len(bo)):
        if bo[pos[0]][i]==num and pos[1] != i:
            return False

    #returns if attempt is false
    for i in range(0, len(bo)):
        if bo[i][pos[1]]==num and pos[1] != i:
            return False
    #box check
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 +3):
            if bo[i][j]==num and (i,j) != pos:
                return False

    return True

def find_emp(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] ==0:
                return(i,j)
    return None


#prints a sudoku board with horizonal and vertical lines seperating the sections  
def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j%3 ==0:
                print(" | ", end="")

            if j==8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j])+ " ", end="")

#This is an example of a sudoku board that requires solving.                
board = [
        [6, 0, 3, 1, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 7],
        [0, 2, 0, 0, 0, 8, 9, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [2, 5, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [5, 9, 8, 0, 3, 0, 0, 0, 2],
        [0, 0, 4, 2, 0, 0, 0, 3, 0]
    ]


pp = pprint.PrettyPrinter(width=41)
solve(board)
pp.pprint(board)





