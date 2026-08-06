class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()       
        n = len(points)

        arrows = 1
        left = points[0][0]
        right = points[0][1]

        for i in range(1, n):
            if points[i][0] <= right:
                left = max(left, points[i][0])
                right = min(right, points[i][1])
            else:
                arrows += 1
                left = points[i][0]
                right = points[i][1]

        return arrows