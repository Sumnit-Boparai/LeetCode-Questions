class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0, 0]
        for i in range(len(nums)):
            cache[0], cache[1] = cache[1], max(nums[i] + cache[0], cache[1])

        return cache[1] 