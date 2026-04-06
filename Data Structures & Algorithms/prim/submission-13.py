class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2, weight in edges:
            adj[n1].append((weight, n2))
            adj[n2].append((weight, n1))

        minHeap = [(0, 0)]
        res = 0
        visited = set()

        while minHeap and len(visited) < n:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            res += weight

            for weight, neighbour in adj[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (weight, neighbour))
        
        return res if len(visited) == n else -1


































        # adj = defaultdict(list)

        # for n1, n2, weight in edges:
        #     adj[n1].append([weight, n2])
        #     adj[n2].append([weight, n1])

        # minHeap = [[0, 0]]
        # visited = set()
        # res = 0

        # while minHeap and len(visited) < n:
        #     weight, node = heapq.heappop(minHeap)

        #     if node in visited:
        #         continue
        #     visited.add(node)

        #     res += weight

        #     for w, neighbour in adj[node]:
        #         if neighbour not in visited:
        #             heapq.heappush(minHeap, [w, neighbour])
        
        # return res if len(visited) == n else -1