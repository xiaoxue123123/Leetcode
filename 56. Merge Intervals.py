
intervals= [[2,3],[4,5],[6,7],[8,9],[1,10]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []

        if len(intervals) == 0:
            res = []

        for new in intervals:
            if len(res) == 0:
                res.append(intervals[0])
            else:
                if new[0] <= res[-1][1] and new[1] >= res[-1][0]:
                    res[-1][0] = min(new[0], res[-1][0])
                    res[-1][1] = max(new[1], res[-1][1])
                else:
                    res.append(new)
        return res

