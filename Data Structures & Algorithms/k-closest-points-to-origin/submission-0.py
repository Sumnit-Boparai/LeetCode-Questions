class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            heapq.heappush(minHeap, [-(point[0] ** 2 + point[1] ** 2), point])
            while len(minHeap) > k:
                heapq.heappop(minHeap)

        res = [point[1] for point in minHeap]

        return res