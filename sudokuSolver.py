board=[["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """

    print("\n")
    for i in range(len(bo)):

        if i%3==0 and i!=0:
            print("------------------------")

        for j in range(len(bo[0])):

            if j%3==0 and j!=0:
                print(" | ",end="")

            if j==8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]),end=" ")

print_board(board)

def is_valid(bo,pos,val):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    val=str(val)
    r,c=pos[0],pos[1]

    for i in range(len(bo)):
        if bo[r][i]==val or bo[i][c]==val:
            return False
        if bo[3*(r//3)+i//3][3*(c//3)+i%3]==val:
            return False  
    return True


def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    n=len(bo)
    for r in range(n):
        for c in range(n):
            if bo[r][c]==".":
                for val in range(n):
                    val+=1
                    if(is_valid(bo,(r,c),str(val))):
                        bo[r][c]=str(val)
                        nextSol=solve(bo)

                        if(nextSol==True):
                            return True
                        else:
                            bo[r][c]="."
                return False
    return True

solve(board)
print_board(board)

