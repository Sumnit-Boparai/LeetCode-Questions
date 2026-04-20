class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for srcPoint in points:
            srcPoint = tuple(srcPoint)
            for destPoint in points:
                destPoint = tuple(destPoint)
                distance = (abs(srcPoint[0] - destPoint[0]) + abs(srcPoint[1] - destPoint[1]))
                adj[srcPoint].append((distance, destPoint))
            
        minHeap = [(0, tuple(points[0]))]
        visited = set()
        res = 0

        while minHeap and len(visited) < len(points):
            distance, src = heapq.heappop(minHeap)

            if src in visited:
                continue
            
            res += distance
            visited.add(src)

            for neighbour in adj[src]:
                if neighbour[1] not in visited:
                    heapq.heappush(minHeap, neighbour)
            
        return res