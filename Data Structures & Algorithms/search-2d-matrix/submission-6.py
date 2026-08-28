class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        size = (ROWS * COLS) - 1
        l, r = 0, size
        while l <= r:
            m = (l + r) // 2
            row, col = m // COLS, m % COLS
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        return False
