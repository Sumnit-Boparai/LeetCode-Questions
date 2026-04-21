class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        cache = [0] * (COLS+1)
        cache[1] = 1
        
        for r in range(1, ROWS+1):
            nextCache = [0] * (COLS+1)
            for c in range(1, COLS+1):
                nextCache[c] = cache[c] + nextCache[c-1]
            cache = nextCache
        return cache[-1]