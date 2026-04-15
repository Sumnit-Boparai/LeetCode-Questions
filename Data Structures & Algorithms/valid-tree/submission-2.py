class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def join(self, x, y) -> bool:
        findX = self.find(x)
        findY = self.find(y)

        if findX != findY:
            if self.size[findX] >= self.size[findY]:
                self.parents[findY] = findX
                self.size[findX] += self.size[findY]
            else:
                self.parents[findX] = findY
                self.size[findY] += self.size[findX]
            return True
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        unionFind = UnionFind(n)
        components = 0

        for source, dest in edges:
            if not unionFind.join(source, dest):
                return False
            components += 1

        return components == n - 1
