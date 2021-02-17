nums = [1,3,4,2,2]

# performance is good, my own solution
# h = {}
# for i in nums:
#     if i not in h:
#         h[i]=1
#     else:
#         print(i)

# use linked list
# Floyd's Tortoise and Hare (Cycle Detection)

# phase1: find where t and h meet
t = 0
h = 0
t = nums[t]
h = nums[nums[h]]

while t!=h:
    t = nums[t]
    h = nums[nums[h]]
# phase2: t starts at 0, h starts at intersection.
# where they meet will be start of cycle.
t = 0
while t!=h:
    t = nums[t]
    h = nums[h]
print(h)