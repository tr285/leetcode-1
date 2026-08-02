class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        idx ={}
        for i in range(len(nums)):
            if nums[i] in idx:
                if i-idx[nums[i]]<=k:
                 return True
            idx[nums[i]] =i
           
        return False