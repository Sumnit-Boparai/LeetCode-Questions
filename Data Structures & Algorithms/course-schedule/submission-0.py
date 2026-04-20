class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, preq in prerequisites:
            adj[course].append(preq)
        
        path = set()
        visited = set()

        def dfs(node) -> bool:
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False
            path.remove(node)
            visited.add(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True