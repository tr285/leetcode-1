class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current =nums[0]
        maximum = nums[0]
        for i in range(1,len(nums)):
            if current +nums[i]>nums[i]:
                current=current+nums[i]
            else:
                current=nums[i]
            if current>maximum:
                maximum=current
        return maximum