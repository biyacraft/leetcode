"""Given an array and a value, remove all instances of that value in place and return
the new length.
Do not allocate extra space for another array, you must do this in place with
constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond
the new length.
Example: Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
URL: https://leetcode.com/problems/remove-element/
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val == []:
            return 0
        else:
            i = 0
            j = 0
            while j < len(nums):
                if nums[j] == val:
                    j += 1
                else:
                    nums[i] = nums[j]
                    i += 1
                    j += 1
            return len(nums[0:i])
