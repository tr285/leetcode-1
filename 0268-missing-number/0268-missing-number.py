class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total =n*(n+1)//2
        current = 0
        for num in nums:
            current+=num

        return total -current
