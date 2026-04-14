class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        res = []
        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
