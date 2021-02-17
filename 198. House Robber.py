# bottom up problem
# local maximum adds up to global maximum

#nums = [2,7,9,3,1]
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
import time

#自己的solution，timeout了
def dp(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0:2])
    else:
        return max(dp(nums[:-2])+nums[-1],dp(nums[:-1]))


start_time = time.time()
dp(nums)
print("--- %s seconds ---" % (time.time() - start_time))


# 网上的solution 快很多

start_time = time.time()
res = [0] * (len(nums) + 1)
res[0] = 0
if len(nums) > 0:
    res[1] = nums[0]
if len(nums) > 1:
    res[2] = max(nums[0:2])
    for i in range(2, len(nums)):
        res[i + 1] = max(res[i - 1] + nums[i], res[i])

print("--- %s seconds ---" % (time.time() - start_time))

