class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in indexMap and i != indexMap[difference]:
                return[indexMap[difference], i]
            indexMap[num] = i