class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt, end = 0, -float('inf')
        points = sorted(points, key = lambda x: x[1])
        for s, e in points:
            if s > end:
                cnt += 1
                end = e
        return cnt

