class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0, 1, 1]
        res = 0
        if n < 3:
            return cache[n]
        
        for i in range(3, n+1):
            cache[i%3] = sum(cache)
        
        return cache[n%3]