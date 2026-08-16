class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr =nums[0]
        ans =nums[0]
        for i in range(1,len(nums)):
           curr= max(nums[i],curr+nums[i])
           ans= max(ans,curr)
        return ans
        