""" Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.
URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            start = 0
            end = len(nums) - 1
            return self.to_bst(nums, start, end)
   
    def to_bst(self, arr, start, end):
        if len(arr) == 0 or start > end:
        return None
        else:
            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            node.left = self.to_bst(arr, start, mid - 1)
            node.right = self.to_bst(arr, mid + 1, end)
                return node
