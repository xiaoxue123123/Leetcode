nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# merge sort
nums1[:] = sorted(nums1[:m] + nums2)

# quicksort
x = nums2.pop()
for i in range(m):
    if nums1[i]>x:
        nums1[i] = x


#sorted(nums1[0:m] + nums2[0:n])
