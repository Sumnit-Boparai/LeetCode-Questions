# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node)-> (int, bool):
            if not node:
                return (0, True)
            dfsLeft = dfs(node.left)
            dfsRight = dfs(node.right)

            balanced = abs(dfsLeft[0] - dfsRight[0]) <= 1 and dfsLeft[1] and dfsRight[1]
            
            return (1 + max(dfsLeft[0], dfsRight[0]), balanced)

        return dfs(root)[1]