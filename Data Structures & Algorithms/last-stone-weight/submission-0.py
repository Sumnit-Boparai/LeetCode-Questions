class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stones[x] for x in range(len(stones))]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = abs(heapq.heappop(maxHeap))
            y = abs(heapq.heappop(maxHeap))

            if x != y:
                res = abs(x - y)
                heapq.heappush(maxHeap, -res)
        
        return 0 if len(maxHeap) == 0 else abs(maxHeap[0])