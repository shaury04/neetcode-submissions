class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                n = board[r][c]
                if n in row[r] or n in col[c] or n in sqr[(r//3, c//3)]:
                    return False
                row[r].add(n)
                col[c].add(n)
                sqr[(r//3, c//3)].add(n)
        return True
