class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [grid[0][0]] * COLS
        
        for c in range(1, COLS):
            cache[c] = grid[0][c] + cache[c-1] 

        for r in range(1, ROWS):
            newCache = [0] * COLS
            for c in range(COLS):
                if c > 0:
                    newCache[c] = grid[r][c] + min(cache[c], newCache[c-1])
                else:
                    newCache[c] = grid[r][c] + cache[c]
            cache = newCache

        return cache[-1]
