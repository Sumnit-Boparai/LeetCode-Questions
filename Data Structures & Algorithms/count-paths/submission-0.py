class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [0] * (n + 1)
        cache[n-1] = 1

        for r in range(m-1, -1, -1):
            newRow = [0] * (n + 1)
            for c in range(n-1, -1, -1):
                newRow[c] += cache[c] + newRow[c+1]
            cache = newRow
        return cache[0]