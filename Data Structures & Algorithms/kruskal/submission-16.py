class UnionFind:
    def __init__(self, n:int):
        self.parents = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x:int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def join(self, x:int, y:int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parents[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parents[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            return True
        return False 


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for n1, n2, weight in edges:
            heapq.heappush(minHeap, (weight, n1, n2))

        components = 0
        res = 0
        unionFind = UnionFind(n)

        while minHeap and components < n-1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.join(n1, n2):
                res += weight
                components += 1
        
        return res if components == n-1 else -1

        
            




























# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = [i for i in range(n)]
#         self.size = [1] * n
#         print(self.parent, self.size)
    
#     def find(self, x: int) -> int:
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x: int, y: int) -> bool:
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX != rootY:
#             if self.size[rootX] < self.size[rootY]:
#                 self.parent[rootX] = rootY
#                 self.size[rootY] += self.size[rootX]
#             else:
#                 self.parent[rootY] = rootX
#                 self.size[rootX] += self.size[rootY]
#             return True
#         return False

# class Solution:
#     def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
#         minHeap = []
#         for n1, n2, weight in edges:
#             heapq.heappush(minHeap, [weight, n1, n2])
        
#         unionFind = UnionFind(n)
#         res, components = 0, 0

#         while minHeap and components < n - 1:
#             weight, n1, n2 = heapq.heappop(minHeap)
            
#             if unionFind.union(n1, n2):
#                 res += weight
#                 components += 1
        
#         return res if components == n - 1 else -1
