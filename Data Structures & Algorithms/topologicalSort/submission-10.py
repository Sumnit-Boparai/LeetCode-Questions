class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for source, dest in edges:
            adj[source].append(dest)

        visited = set()
        path = set()
        res = []

        def dfs(node) -> bool:
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False
            path.remove(node)
            visited.add(node)
            res.append(node)
            
            return True

        for i in range(n):
            if not dfs(i):
                return []

        res.reverse()
        return res






























        # adj = defaultdict(list)
        # for source, dest, in edges:
        # adj[source].append(dest)
        # topSort = []
        # visited = set()
        # path = set()

        # def dfs(src: int) -> bool:
        #     if src in visited:
        #         return True
        #     if src in path:
        #         return False
            
        #     path.add(src)
        #     for neighbour in adj[src]:
        #         if not dfs(neighbour):
        #             return False
        #     path.remove(src)
        #     visited.add(src)
        #     topSort.append(src)

        #     return True
        
        # for i in range(n):
        #     if not dfs(i):
        #         return []
        
        # topSort.reverse()
        # return topSort