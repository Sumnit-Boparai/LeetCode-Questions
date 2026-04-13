class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, visited):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 1 or (r, c) in visited:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            res = 0
            visited.add((r, c))
            
            for nr, nc in directions:
                res += dfs(r + nr, c + nc, visited)
            
            visited.remove((r, c))
            return res

        return dfs(0, 0, set())







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # ROWS, COLS = len(grid), len(grid[0])

        # def dfs(r, c, visited):
        #     if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 1:
        #         return 0

        #     if r == ROWS - 1 and c == COLS - 1:
        #         return 1

        #     visited.add((r, c))
        #     res = 0
        #     for nr, nc in directions:
        #         res += dfs(r + nr, c + nc, visited)
        #     visited.remove((r, c))
        #     return res
        
        # return dfs(0, 0, set())