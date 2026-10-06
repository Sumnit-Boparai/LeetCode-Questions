class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1, 0]
        for step in range(n-1, -1, -1):
            cache = [cache[0] + cache[1], cache[0]]
            

        return cache[0]

        
        #state(i) represents the number of distinct ways to get from i to the top
        #each state we have a choice of 1 or two steps
        #we get the distinct ways from both states and add them together since they are both possibilites
        #base case will be 0 if we reach the above top or 1 if we reach the top
        #this goes through all possible paths, but we can save time and space by only using the states and storing the states. If two paths reach the same state, they have the same subproblem to compute, so we dont need to do it multiple times, we do it once and cache the result for furture use. We can use the step we are at as enough information to know we are sending the correct information for the state they are in.
        #we can tell that we only need the result from the two steps above the current step to get the solution from the current step, so we only need to store and update those two values and use them to caclucate the result from right to left and find the final answer.
