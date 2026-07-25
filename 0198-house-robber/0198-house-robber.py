class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 =0
        prev2 =0
        for num in nums:
            curr = max(prev2,prev1 + num)
            prev1 = prev2
            prev2 = curr
        return prev2