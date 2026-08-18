class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_digit =[-1]*10
        ans =-1
        for num in nums:
            temp =num
            largest =0
            while temp >0:
               digit =temp%10
               largest =max(largest,digit)
               temp//=10
            if max_digit[largest] !=-1:
               ans =max(ans,num+max_digit[largest])
            max_digit[largest] =max(max_digit[largest],num)
        return ans
