class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, dest, weight in times:
            adj[source].append((weight, dest))

        minHeap = [[0, k]]
        visited = set()
        res = 0

        while minHeap and len(visited) < n:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, weight)

            for w, neighbour in adj[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (w + weight, neighbour))

        return res if len(visited) == n else -1