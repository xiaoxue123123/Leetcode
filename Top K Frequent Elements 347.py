nums = [1,1,1,1,2,2,3]
k=2

from itertools import chain
freq = {}
for i in nums:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
# solution 1 (看了答案后自己写的）
# bucket = [[] for _ in range(len(nums)+1)]
# # 创建一个bucket按照从小到大的顺序存num
#
# for i,v in freq.items():
#     bucket[v].append(i)
#
# flat_list = list(chain(*bucket))
#
# # 返回top k num
# print(flat_list[::-1][:k])


# solution 2 时间空间都比第1个快
# 按照frequency(value)排序
srt = sorted(freq.items(), key=lambda x: x[1])
# return top k 的key
print([x[0] for x in srt[::-1][:k]])





# 网上的答案
from collections import Counter
from itertools import chain
def topKFrequent(self, nums, k):
    bucket = [[] for _ in range(len(nums) + 1)]
    Count = Counter(nums).items()
    for num, freq in Count: bucket[freq].append(num)
    flat_list = list(chain(*bucket))
    return flat_list[::-1][:k]

