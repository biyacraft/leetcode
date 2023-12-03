class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        
       
        current_sum = float(sum(nums[:k]))
        
       
        max_sum = current_sum
        
       
        for i in range(k, n):
            current_sum = current_sum - nums[i - k] + nums[i]
            
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
