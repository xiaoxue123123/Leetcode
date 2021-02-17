nums = [-2,1,-3,4,-1,2,1,-5,4]




# divide and conquer, 网上的答案
def cross_sum(self, nums, left, right, p):
    if left == right:
        return nums[left]

    left_subsum = float('-inf')
    curr_sum = 0
    for i in range(p, left - 1, -1):
        curr_sum += nums[i]
        left_subsum = max(left_subsum, curr_sum)

    right_subsum = float('-inf')
    curr_sum = 0
    for i in range(p + 1, right + 1):
        curr_sum += nums[i]
        right_subsum = max(right_subsum, curr_sum)

    return left_subsum + right_subsum


def helper(self, nums, left, right):
    if left == right:
        return nums[left]

    p = (left + right) // 2

    left_sum = self.helper(nums, left, p)
    right_sum = self.helper(nums, p + 1, right)
    cross_sum = self.cross_sum(nums, left, right, p)

    return max(left_sum, right_sum, cross_sum)


def maxSubArray(self, nums: 'List[int]') -> 'int':
    return self.helper(nums, 0, len(nums) - 1)












# 自己写一遍 greedy
cur_sum = max_sum = nums[0]

for i in range(len(nums)):
    cur_sum = max(nums[i],cur_sum+nums[i]) # 相当于选出local opitimal from greedy algorithm
    max_sum = max(cur_sum,max_sum)

print(max_sum)





# Greedy
# n = len(nums)
# curr_sum = max_sum = nums[0]
#
# for i in range(1, n):
#     curr_sum = max(nums[i], curr_sum + nums[i])
#     max_sum = max(max_sum, curr_sum)
#
# print(max_sum)

nums = [-2,1,-3,4,-1,2,1,-5,4]
# 自己写一遍 dynamic programming

for i in range(0,len(nums)-1):
    if nums[i] > 0:
        nums[i+1] += nums[i]
    max_sum = max(max_sum,nums[i+1])











# Dynamic Programming
n = len(nums)
max_sum = nums[0]
for i in range(1, n):
    print('i',i)
    print('nums[i]-1', nums[i-1])
    if nums[i - 1] > 0:
        print('nums[i]0', nums[i])
        nums[i] += nums[i - 1] # only when previous sum was positive, add previous sum
        # and update current element
        print('nums[i]1',nums[i])
    print('max_sum0', max_sum)
    max_sum = max(nums[i], max_sum) # find max between previous max and current max
    print('max_sum1',max_sum)



print(max_sum)