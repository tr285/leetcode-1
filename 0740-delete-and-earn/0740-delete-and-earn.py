class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_num = max(nums)
        points =[0] * (max_num +1)
        for num in nums:
            points[num] += num
        prev1 =0
        prev2 =0
        for point in points:
            curr = max(prev2,prev1 + point)
            prev1 = prev2
            prev2 = curr
        return prev2