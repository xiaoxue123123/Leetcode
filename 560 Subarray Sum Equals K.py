nums = [1,1,1]
k = 2



# solution1: O(n^3)
# for i in range(len(nums)):
#     if nums[i] == k:
#         res += 1
#     pass
#     for j in range(i+1,len(nums)):
#         if sum(nums[i:j+1])==k:
#             res += 1

# solution 2: cumulative sum, 还是太慢
# res = 0
#
# s = [0]
#
# for i in range(1,len(nums)+1):
#     s.append(s[-1]+nums[i-1])
#
#
#
# for i in range(0,len(s)):
#     for j in range(i+1,len(s)):
#         if s[j] - s[i] == k:
#             res += 1


## solution 3: 网上的答案
import collections
running_sum = 0
hash_table = collections.defaultdict(lambda: 0)
total = 0
for x in nums:
    print('x',x)
    running_sum += x
    sum = running_sum - k
    #sum就是和running_sum相隔k，如果sum出现过，running_sum也一定
    #出现过，那么就算作一次。
    if sum in hash_table:
        total += hash_table[sum]
    if running_sum == k:
    #如果是从头开始加等于k，也算作一次。
        total += 1
    hash_table[running_sum] += 1
    #running_sum就是从头开始出现过的sum
    print('sum',sum,'total',total,'running_sum',running_sum)