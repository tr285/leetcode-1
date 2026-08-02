class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check ={}
        for i in range(len(nums)):
            total = target - nums[i]
            if total in check:
                return[check[total],i]
            check[nums[i]] = i