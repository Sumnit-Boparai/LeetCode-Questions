class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(countOpen, countClosed, combination):
            if len(combination) == (n * 2):
                res.append("".join(combination))
            
            if countOpen < n:
                combination.append('(')
                dfs(countOpen + 1, countClosed, combination)
                combination.pop()
            
            if countClosed < countOpen:
                combination.append(')')
                dfs(countOpen, countClosed + 1, combination)
                combination.pop()
        
        dfs(0, 0, [])
        return res
    