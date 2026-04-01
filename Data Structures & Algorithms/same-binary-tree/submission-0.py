# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque()
        queueQ = deque()
        queueP.append(p)
        queueQ.append(q)

        while queueP and queueQ:
            for _ in range(len(queueP)):
                nodeP = queueP.popleft()
                nodeQ = queueQ.popleft()

                if not nodeQ and not nodeP:
                    continue
                elif (not nodeQ and nodeP) or (nodeQ and not nodeP) or (nodeQ.val != nodeP.val):
                    return False
                queueP.append(nodeP.left)
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.left)
                queueQ.append(nodeQ.right)
        return True