"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its
center).
Note: Bonus points if you could solve it both recursively and iteratively.
URL: https://leetcode.com/problems/symmetric-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            if root1.val == root2.val:
                return self.isMirror(root1.left, root2.right) an
d self.isMirror(root1.right, root2.left)
            else:
                return False


