class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1

        cache = [[-1] * COLS for _ in range(ROWS)]

        def dfs(i, capacity) -> int:
            if i == len(profit):
                return 0
            if cache[i][capacity] != -1:
                return cache[i][capacity]
            
            newCapacity = capacity - weight[i]
            
            if newCapacity >= 0:
                cache[i][capacity] = max(dfs(i+1, capacity), profit[i] + dfs(i, newCapacity))
            else:
                cache[i][capacity] = dfs(i+1, capacity)
            
            return cache[i][capacity]

        return dfs(0, capacity)






























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