class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
            if queue:
                res += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return res
