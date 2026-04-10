class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for nr, nc in directions:
                area += dfs(r + nr, c + nc)
            
            return area
        
        def getAreas():
            res = 0

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        res = max(res, dfs(r, c))
            return res

        return getAreas()