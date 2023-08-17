# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #Make use of recursion
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False

        return self.isSameTree(p.left,q.left) & self.isSameTree(p.right, q.right)
        
