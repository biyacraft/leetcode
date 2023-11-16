# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        self.helper(root, targetSum, [], result)
        return result

    def helper(self, node, targetSum, path, result):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and node.val == targetSum:
            result.append(path[:])

        self.helper(node.left, targetSum - node.val, path, result)
        self.helper(node.right, targetSum - node.val, path, result)

        path.pop()
