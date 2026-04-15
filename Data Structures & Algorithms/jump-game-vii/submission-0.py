class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        cache = {}
        def dfs(i):
            
            if s[i] == '0':
                if i == len(s)-1:
                    return True
                if i in cache:
                    return cache[i]
                
                for j in range(min(i + maxJump, len(s)-1), i + minJump - 1, -1):
                    if dfs(j):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False

        return dfs(0)