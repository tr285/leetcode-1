class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_s = set(nums)
        lng=0
        for n in num_s:
            if (n-1) not in num_s:
                length =1
                while (n+length) in num_s:
                    length +=1
                lng = max(lng,length)
        return lng