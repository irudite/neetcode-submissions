class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            duplicates = set()
            for j in range(9):
                if board[i][j] in duplicates:
                    return False
                elif board[i][j] == ".":
                    continue
                duplicates.add(board[i][j])

        for i in range(9):
            duplicates = set()
            for j in range(9):
                if board[j][i] in duplicates:
                    return False
                elif board[j][i] == ".":
                    continue
                duplicates.add(board[j][i])

        for square in range(9):
            duplicates = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in duplicates:
                        return False
                    elif board[row][col] == ".":
                        continue
                    duplicates.add(board[row][col])

        return True