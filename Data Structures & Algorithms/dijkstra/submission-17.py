class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for source, dest, weight in edges:
            adj[source].append((weight, dest))
        
        minHeap = [[0, src]]
        res = {}

        while minHeap and len(res) < n:
            weight, node = heapq.heappop(minHeap)

            if node in res:
                continue
            
            res[node] = weight

            for w, neighbour in adj[node]:
                if neighbour not in res:
                    heapq.heappush(minHeap, (w + weight, neighbour))
        
        for i in range(n):
            if i not in res:
                res[i] = -1

        return res








        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # adj = defaultdict(list)
        
        # for source, destination, weight in edges:
        #     adj[source].append([weight, destination])

        # shortest = {}
        # minHeap = [[0, src]]

        # while minHeap:
        #     w1, n1 = heapq.heappop(minHeap)
        #     if n1 in shortest:
        #         continue
        #     shortest[n1] = w1

        #     for weight, neighbour in adj[n1]:
        #         if neighbour not in shortest:
        #             heapq.heappush(minHeap, [w1 + weight, neighbour])
        
        # for node in range(n):
        #     if node not in shortest:
        #         shortest[node] = -1
        
        # return shortest

