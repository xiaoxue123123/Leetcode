class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        output: x, y of right segment.


        '''

        res = []
        buildLines = []
        for points in buildings:
            buildLines.append([points[0], -points[2]])
            buildLines.append([points[1], points[2]])

        buildLines = sorted(buildLines, key=lambda x: (x[0], x[1]))

        maxHeap = [0]

        preHi = 0
        for points in buildLines:
            if points[1] < 0:
                heappush(maxHeap, points[1])
            else:
                if -points[1] in maxHeap:
                    maxHeap.remove(-points[1])
                    heapq.heapify(maxHeap)
            curHeight = -maxHeap[0]
            if curHeight != preHi:
                res.append([points[0], curHeight])
                preHi = curHeight
        return res