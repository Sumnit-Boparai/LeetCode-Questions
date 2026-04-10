class Solution:
    def rob(self, nums: List[int]) -> int:

        def simulate(start, end):
            cache = [0, 0]
            for i in range(start, end):
                cache[0], cache[1] = cache[1], max(cache[1], nums[i] + cache[0])
            return max(cache)

        if len(nums) < 2:
            return nums[0]
        return max(simulate(0, len(nums)-1), simulate(1, len(nums)))

