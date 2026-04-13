"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque()
        cache = {}
        cache[node] = Node(node.val)
        queue.append(node)

        while queue:
            n = queue.popleft()
            copy = cache[n]
            for neighbor in n.neighbors:
                if neighbor not in cache:
                    cache[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                copy.neighbors.append(cache[neighbor])
            
        return cache[node]
