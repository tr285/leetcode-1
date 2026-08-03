class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res
        st =nums[0]
        for i in range(len(nums)):
            if i ==len(nums)-1 or nums[i] +1 !=nums[i+1]:
                if st ==nums[i]:
                    res.append(str(st))
                else:
                    res.append(str(st)+"->"+str(nums[i]))
                if i!= len(nums)-1:
                    st =nums[i+1]
        return res