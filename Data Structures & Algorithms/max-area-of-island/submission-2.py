class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        def bfs(r,c):
            visited.add((r,c))
            q = deque()
            area = 1
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS \
                    or (nr,nc) in visited or grid[nr][nc] != 1:
                        continue
                    area += 1
                    q.append((nr,nc))
                    visited.add((nr,nc))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r,c), maxArea)
        return maxArea