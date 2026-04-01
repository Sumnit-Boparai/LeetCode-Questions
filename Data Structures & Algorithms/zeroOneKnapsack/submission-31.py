class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1

        cache = [0] * COLS

        for i in range(ROWS):
            newRow = [0] * COLS
            for capacity in range(COLS):
                newCapacity = capacity - weight[i]

                if newCapacity >= 0:
                    newRow[capacity] = max(cache[capacity], profit[i] + cache[newCapacity])
                else:
                    newRow[capacity] = cache[capacity]
            cache = newRow
        return cache[-1]















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Dynamic Programming Memory Optimized
        # ROWS, COLS = len(profit), capacity + 1
        # dp = [0] * COLS

        # for cap in range(COLS):
        #     if weight[0] <= cap:
        #         dp[cap] = profit[0]
        
        # for i in range(1, ROWS):
        #     currRow = [0] * COLS
        #     for cap in range(1, COLS):
        #         newCapacity = cap - weight[i]

        #         if newCapacity >= 0:
        #             currRow[cap] = max(dp[cap], profit[i] + dp[newCapacity])
        #         else:
        #             currRow[cap] = dp[cap]
            
        #     dp = currRow
        # return dp[capacity]        
        
        #Dynamic Programming
        
        # ROWS, COLS = len(profit), capacity + 1
        # dp = [[0] * COLS for _ in range(ROWS)]

        # for cap in range(COLS):
        #     if weight[0] <= cap:
        #         dp[0][cap] = profit[0]
        
        # for i in range(1, ROWS):
        #     for cap in range(1, COLS):
        #         newCapacity = cap - weight[i]

        #         if newCapacity >= 0:
        #             dp[i][cap] = max(dp[i-1][cap], profit[i] + dp[i-1][newCapacity])
        #         else:
        #             dp[i][cap] = dp[i-1][cap]
        
        # return dp[ROWS - 1][capacity]


        #Brute Force
        # def dfs(index, capacity):
        #     if index == len(profit):
        #         return 0

        #     newCapacity = capacity - weight[index]
            
        #     if newCapacity >= 0:
        #         return max(dfs(index + 1, capacity), profit[index] + dfs(index + 1, newCapacity))
        #     else:
        #         return dfs(index + 1, capacity)

        # return dfs(0, capacity)
            