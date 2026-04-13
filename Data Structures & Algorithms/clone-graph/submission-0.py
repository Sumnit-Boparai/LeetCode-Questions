"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cache = {}

        def dfs(n):

            if n in cache:
                return cache[n]
        
            cache[n] = Node(n.val)
            
            for neighbor in n.neighbors:
                cache[n].neighbors.append(dfs(neighbor))
            
            return cache[n]
        
        dfs(node)
        return cache[node]

