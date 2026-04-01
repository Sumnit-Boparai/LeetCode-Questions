class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0, 0]
        for step in range(len(cost)-1, -1, -1):
            cache[0], cache[1] = cost[step] + min(cache[0], cache[1]), cache[0]
        
        return min(cache)