class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sqn = set(nums)
        long_set =0
        for num in sqn:
            if num-1 not in sqn:
                current =num
                length =1
                while current +1 in sqn:
                    current +=1
                    length +=1
                long_set =max(long_set,length)
        return long_set
