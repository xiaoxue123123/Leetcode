class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort()
        slots2.sort()
        l1 = len(slots1)
        l2 = len(slots2)
        i, j = 0, 0
        one = []
        two = []
        while i < l1 and j < l2:
            one = slots1[i]
            two = slots2[j]
            # print(one, two)
            # print(len(one),len(two))
            # print(i, j)
            if len(two) == 0 or len(one) == 0:
                return []

            end = min(one[1], two[1])
            start = max(one[0], two[0])
            if end - start >= duration:
                return [start, start + duration]
            if one[1] > two[1]:
                j += 1
            else:
                i += 1

        return []




