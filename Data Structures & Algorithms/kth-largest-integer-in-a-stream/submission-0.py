class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums.copy()
        heapq.heapify(self.minHeap)
        self.maxSize = k
        self.ensureMinHeapSize()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.ensureMinHeapSize()
        return self.minHeap[0]
    
    def ensureMinHeapSize(self):
        while len(self.minHeap) > self.maxSize:
            heapq.heappop(self.minHeap)
        
