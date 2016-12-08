# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepthx(root, 0)

    def maxDepthx(self, root, depth):
        if not root:
            return depth
        else:
            depth += 1
        leftDepth = self.maxDepthx(root.left, depth)
        rightDepth = self.maxDepthx(root.right, depth)
        return leftDepth if leftDepth > rightDepth else rightDepth
