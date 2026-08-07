class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            dupes = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dupes:
                    return False
                dupes.add(board[i][j])

        for i in range(len(board)):
            dupes = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in dupes:
                    return False
                dupes.add(board[j][i])

        for square in range(9):
            dupes = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in dupes:
                        return False
                    dupes.add(board[row][col])

        return True