#https://leetcode.com/problems/search-insert-position/description/


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Target not found, return the position where it should be inserted

"""
# Examples
nums1, target1 = [1, 3, 5, 6], 5
nums2, target2 = [1, 3, 5, 6], 2
nums3, target3 = [1, 3, 5, 6], 7

print(search_insert(nums1, target1))  # Output: 2
print(search_insert(nums2, target2))  # Output: 1
print(search_insert(nums3, target3))  # Output: 4
"""
