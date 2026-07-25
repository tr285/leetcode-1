class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        if n ==1 or n ==2:
            return 1
        first =0
        second =1
        third =1

        for _ in range(3,n+1):
            first ,second,third = second,third,first +second+third
        return third