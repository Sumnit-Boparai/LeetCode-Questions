class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        cache = [0] * COLS
        
        for i in range(ROWS):
            newRow = [0] * COLS
            for capacity in range(COLS):
                newCapacity = capacity - weight[i]

                if newCapacity >= 0:
                    newRow[capacity] = max(cache[capacity], profit[i] + newRow[newCapacity])
                else:
                    newRow[capacity] = cache[capacity]

            cache = newRow
        
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