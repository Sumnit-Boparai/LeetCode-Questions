class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(i, total):
            nonlocal res
            if i == len(nums):
                res += total
                return
            
            dfs(i+1, total)
            
            total ^= nums[i]
            dfs(i+1, total)

        dfs(0, 0)
        return res