nums = [0,1,0,3,12]


nums.sort(key=bool, reverse=1)
# treat 0 as False, positive number as True
# bool sorting will prioritize False first, and keep other number
# the same. reverse is to put 0 last.

for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(0)
        nums.remove(0)

# remove always remove from the left 