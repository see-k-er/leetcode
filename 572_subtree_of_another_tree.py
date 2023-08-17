# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def sametree(s,t):
            if not s and not t:
                return True
            if (s and t) and s.val == t.val:
                return sametree(s.left,t.left) and sametree(s.right, t.right)
            return False

        if not subRoot: 
            return True
        if not root:
            return False
        
        if sametree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        
