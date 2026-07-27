class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f1 =0
        f2 =0
        for num in nums:
            if num > f1:
                f2 = f1
                f1 = num
            elif num >f2:
                f2 = num
        return (f1-1)*(f2-1)

          


        