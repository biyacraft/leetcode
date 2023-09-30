"""

Given a binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path does
not need to go through the root.
For example: Given the below binary tree,
1
/ \
2 3
Return 6
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.maxSum = -sys.maxint - 1
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.findMax(root)
        return self.maxSum

    def findMax(self,root):
        if root == None:
            return 0
        left = self.findMax(root.left)
        right = self.findMax(root.right)
        self.maxSum = max(root.val + left + right, self.maxSum)
        ret = root.val + max(left,right)
        if ret < 0:
            return 0
        else:
            return ret
