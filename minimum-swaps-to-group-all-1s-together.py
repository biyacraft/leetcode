class Solution:

  
    def minSwaps(self, nums: List[int]) -> int:
        count_ones = sum(nums)
        n = len(nums)
        current_ones = sum(nums[:count_ones])
        max_ones = current_ones
      
        for i in range(count_ones, count_ones + n):
            current_ones += nums[i % n] - nums[i - count_ones]
            max_ones = max(max_ones, current_ones)
        return count_ones - max_ones
