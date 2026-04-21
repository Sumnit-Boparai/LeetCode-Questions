class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [float('inf')] * (COLS+1)
        cache[1] = 0
        
        for r in range(1, ROWS+1):
            for c in range(1, COLS+1):
                cache[c] = grid[r-1][c-1] + min(cache[c], cache[c-1])
        return cache[-1]
