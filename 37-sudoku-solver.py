class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """

        def is_valid(row, col, num):
            # Check row
            for c in range(9):
                if board[row][c] == num:
                    return False

            # Check column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def backtrack():
            for row in range(9):
                for col in range(9):

                    # Skip filled cells
                    if board[row][col] != ".":
                        continue

                    # Try numbers 1-9
                    for num in "123456789":

                        if is_valid(row, col, num):
                            board[row][col] = num

                            # Continue solving
                            if backtrack():
                                return True

                            # Undo the choice
                            board[row][col] = "."

                    # No number works
                    return False

            # Board completely solved
            return True

        backtrack()