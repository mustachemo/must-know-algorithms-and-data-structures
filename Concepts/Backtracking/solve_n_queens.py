def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check if there's a queen in the left-upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check if there's a queen in the left-lower diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return solutions


if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()
