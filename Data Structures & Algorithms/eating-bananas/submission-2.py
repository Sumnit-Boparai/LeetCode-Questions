class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = l + (r - l) // 2
            timeElapsed = 0
            for pile in piles:
                timeElapsed += math.ceil(pile / k)
            if timeElapsed > h:
                l = k + 1
            else:
                r = k - 1
        return l
