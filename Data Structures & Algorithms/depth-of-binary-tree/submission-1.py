# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def DFS(root, depth):
            if root is None: 
                return depth

            left = DFS(root.left, depth+1)
            right = DFS(root.right, depth+1)

            return max(left, right)
            
        return DFS(root, 0)