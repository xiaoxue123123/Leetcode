class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        cnt, end = 0, -float('inf')
        for s,e in intervals:
            if e > end:
                cnt += 1
                end = e
        return cnt

