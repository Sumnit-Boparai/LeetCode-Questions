class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        cache = [0] * COLS
        
        for i in range(ROWS):
            newCache = [0] * COLS
            for c in range(COLS):
                newCap = c - weight[i]

                if newCap >= 0:
                    newCache[c] = max(cache[c], profit[i] + newCache[newCap])
                else:
                    newCache[c] = cache[c]
            cache = newCache
        
        return cache[-1]






























#DP Memory Optimized
#  ROWS, COLS = len(profit), capacity + 1
#     dp = [0] * COLS

#     for c in range(COLS):
#         if weight[0] <= c:
#             dp[c] = profit[0]

#     for i in range(ROWS):
#         newRow = [0] * COLS
#         for c in range(COLS):
#             newCapacity = c - weight[i]
            
#             if newCapacity >= 0:
#                 newRow[c] = max(dp[c], profit[i] + newRow[newCapacity])
#             else:
#                 newRow[c] = dp[c]
#         dp = newRow
#     return dp[COLS - 1]