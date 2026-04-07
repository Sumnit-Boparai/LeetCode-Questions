class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in hashmap.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res
