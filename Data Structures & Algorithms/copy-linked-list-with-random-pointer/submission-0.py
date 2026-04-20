"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        
        def dfs(node):
            if not node:
                return None
            
            if node in cache:
                return cache[node]
            
            cache[node] = Node(node.val)
            cache[node].next = dfs(node.next)
            cache[node].random = dfs(node.random)


            return cache[node]

        dfs(head)
        return cache[head] if head else None