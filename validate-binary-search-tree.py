# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif root.right and not root.left:
            if self.minNode(root.right).val <= root.val:
                return False
            else:
                return self.isValidBST(root.right)
        elif root.left and not root.right:
            if self.maxNode(root.left).val >= root.val:
                return False
            else:
                return self.isValidBST(root.left)
        else:
            if self.maxNode(root.left).val >= root.val:
                return False
            elif self.minNode(root.right).val <= root.val:
                return False
            else:
                return self.isValidBST(root.left) and self.isValidBST(root.right)

    def minNode(self, root):
        min_node = root
        while min_node.left:
            min_node = min_node.left
        return min_node

    def maxNode(self, root):
        max_node = root
        while max_node.right:
            max_node = max_node.right
        return max_node


    def list_to_tree(self, nodes):
        self.max_len = len(nodes)
        self.nodes = nodes
        root = TreeNode(self.nodes[0])
        self.get_child(root, 0)
        return root

    def get_child(self, root, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        if left_index < self.max_len:
            root.left = TreeNode(self.nodes[left_index])
            self.get_child(root.left, left_index)
        if right_index < self.max_len:
            root.right = TreeNode(self.nodes[right_index])
            self.get_child(root.right, right_index)

if __name__=='__main__':
    solution = Solution()
    root = solution.list_to_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print root.left.val
    print root.left.left.val
    print root.left.right.val
    print root.right.right.val
    print root.left.right.right.val
    root = solution.list_to_tree([3,1,5,0,2,4,6,None,None,None,3])
    print solution.isValidBST(root)
