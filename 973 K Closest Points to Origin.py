points = [[3,3],[5,-1],[-2,4]]
K = 2

# my solution 1: use hash table
# hash = {}
#
# for i in range(len(points)):
#     hash[i] = points[i][0]**2+points[i][1]**2
#
# hash = sorted(hash.items(),key=lambda x: x[1])
#
# res = [points[i[0]] for i in hash[0:K]]


# my solution 2: sort
points = sorted(points,key=lambda x: x[0]**2 + x[1]**2)

# 网上的solution use minheap
import heapq

heap = []
for point in points:
    dist = point[0] * point[0] + point[1] * point[1]
    heapq.heappush(heap, (-dist, point))
    # push in the negative distance
    if len(heap) > K:
        heapq.heappop(heap)
    # pop out the smallest member (which is
    # the negative of the largest)

print([tuple[1] for tuple in heap])