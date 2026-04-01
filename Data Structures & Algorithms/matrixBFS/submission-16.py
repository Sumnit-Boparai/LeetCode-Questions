class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        res = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return res
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            res += 1

        return -1







        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        
        
        
        
        
        
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # ROWS = len(grid)
        # COLS = len(grid[0])
        
        # queue = deque()
        # queue.append([0, 0])
        
        # visited = set()
        # visited.add((0, 0))
        
        # res = 0
        
        # while queue:
        #     for _ in range(len(queue)):
        #         r, c = queue.popleft()
        #         if r == ROWS - 1 and c == COLS - 1:
        #             return res
        #         for dr, dc in directions:
        #             nr = r + dr
        #             nc = c + dc
        #             if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == 1:
        #                 continue
        #             queue.append([nr, nc])
        #             visited.add((nr, nc))
        #     res += 1
        
        # return -1

