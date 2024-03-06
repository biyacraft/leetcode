"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
https://leetcode.com/problems/3sum/
"""
class Solution(object):
     def threeSum(self, nums):
        res = []
        nums.sort()
        ls = len(nums)
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res
