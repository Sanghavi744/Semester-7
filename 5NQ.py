def solveNQueens(n: int, first_queen_col: int):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    backtrack(1)  # Start with the second row
    return res

if __name__ == "__main__":
    n = 8
    first_queen_col = 1
    board = solveNQueens(n, first_queen_col)[0]
    for row in board:
        print(" ".join(row))


'''The code solves the N-Queens problem, 
placing N queens on an NxN chessboard without attacking each other. 
It uses a backtracking algorithm to explore all possible queen placements.
It maintains sets for columns, positive diagonals, and negative diagonals to 
track valid queen positions. Starting with the first row and the specified
column for the first queen, it recursively explores all valid placements for 
the remaining queens. When a valid solution is found, it's added to the result.
The code then prints the first solution for an 8x8 board with the first 
queen in the 2nd column, demonstrating a valid queen configuration while 
respecting N-Queens rules.'''


'''The N-Queens problem is a classic combinatorial problem in chess and
computer science. It involves placing N chess queens on an NxN 
chessboard so that no two queens threaten each other. In other words, 
no two queens can share the same row, column, or diagonal.
The goal of the N-Queens problem is to find all possible arrangements of queens on 
the board that satisfy these constraints. It's not only a fascinating puzzle 
but also an important problem in algorithm design and artificial intelligence.
Solving the N-Queens problem requires finding all solutions or a single valid 
placement of queens on the chessboard, depending on the specific problem instance.
Various algorithms, including backtracking, can be used to tackle this problem and 
find valid solutions. The N-Queens problem has practical applications
 in areas like optimization, computer vision, and constraint satisfaction problems.'''




