class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            elif i == n:
                return 1
            
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)

        
        #state(i) represents the number of distinct ways to get from i to the top
        #each state we have a choice of 1 or two steps
        #we get the distinct ways from both states and add them together since they are both possibilites
        #base case will be 0 if we reach the above top or 1 if we reach the top
        #this goes through all possible paths, but we can save time and space by only using the states and storing the states. If two paths reach the same state, they have the same subproblem to compute, so we dont need to do it multiple times, we do it once and cache the result for furture use. We can use the step we are at as enough information to know we are sending the correct information for the state they are in.
