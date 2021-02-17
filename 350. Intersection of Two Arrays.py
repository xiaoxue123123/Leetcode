nums1 = [1,2,2,1]
nums2 = [2,2]

s1 = set(nums1)
s2 = set(nums2)

res = []
for s in nums1:
    if s in nums2:
        res.append(s)
        nums2.remove(s)




