#!/usr/bin/python3

"""This task solves the N queens challenge
This arranges n amount of queens on a chessboard
such that no queen attacks another"""

def init(n):
    """This creates a list of lists of size n x n
    and initialises it with blank space"""
    nlist = []
    for row in range(n):
        nlist.append([])
    for i in nlist:
        for col in range(n):
            nlist.append(" ")
    return nlist


def chessboard(nlist):
    """This arranges the list in chessboard format
    of rows and columns"""
    if isinstance(nlist, list):
        return (list(map(chessboard, nlist)))
    return nlist


def get_position(nlist):
    """This returns the position of each queen"""
    solution = []
    for r in range(len(nlist)):
        for c in range(len(nlist)):
            if nlist[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_out(nlist, row, col):
    """This marks out all the position on a board where
    the queen can not reach"""
    # mark out all forward spots
    for c in range(col + 1, len(nlist)):
        nlist[row][c] = "x"
    # marks out all backward spots
    for c in range(col - 1, len(nlist)):
        nlist[row][c] = "x"
    # marks out all spots on the right
    for r in range(row + 1, len(nlist)):
        nlist[r][col] = "x"
    # marks out all spots on the left
    for r in range(row - 1, len(nlist)):
        nlist[r][col] = "x"
    #marks out all spots diagonally to the top right
    c = col + 1
    for r in range(row + 1, len(nlist)):
        if c + 1 >= len(nlist):
            break
        nlist[r][col] = "x"
        c += 1
    #marks out all diagonal spot to the top left
    c = col + 1
    for r in range(row - 1, len(nlist)):
        if c + 1 >= len(nllist):
            break
        nlist[r][col] = "x"
        c += 1
    #marks out all diagonal spot to the bottom right
    c = col - 1
    for r in range(row + 1, len(nlist)):
        if c >= len(nlist):
            break
        nlist[r][col] = "x"
        c -= 1
    #mark out all diagonal spots to the bottom left
    c = col - 1
    for r in range(row + 1, len(nlist)):
        if c >= len(nlist):
            break
        nlist[r][col] = "x"
        c -= 1

def recursive_solve(nlist, row, queens, solution):
    """This solves the n-queen problem
    Args:
        nlist: The currnet working chessboard
        row: The current working row
        queens: The current number of placed queens
        solutions: A list of lists of solutions
    Returns:
        solution
    """
    if queens == len(nlist):
        solution.append(get_position(nlist))
        return solution

    for c in range(len(nlist)):
        if nlist[row][c] == " ":
            temp_board = chessboard(nlist)
            temp_board[row][c] = "Q"
            mark_out(temp_board, row, c)
            solution = recursive_solve(temp_board, row + 1, queens + 1,
                    solution)

    return (solution)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = init(int(sys.argv[1]))
    solution = recursive_solve(board, 0, 0, [])
    for sol in solution:
        print(sol)
