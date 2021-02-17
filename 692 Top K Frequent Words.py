words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

import collections, heapq

# hash table
h = {}
for w in words:
    if w in h:
        h[w]+=1
    else:
        h[w] = 1

# 自己写的sort
h_key = list(h.keys())
h_key.sort(key=lambda x: (-h[x],x))
print(h_key[:k])

# 自己写的heap
# h = [(-int(freq),value) for value,freq in h.items()]
# heapq.heapify(h)
# print([heapq.heappop(h)[1] for _ in range(k)])
#

# 网上的答案 sort
# def topKFrequent(self, words, k):
#     count = collections.Counter(words)
#     candidates = list(count.keys())
#     candidates.sort(key=lambda w: (-count[w],w))
#     return candidates[:k]


# 网上的heap solution
# def topKFrequent(words, k):
#     count = collections.Counter(words)
#     heap = [(-freq, word) for word, freq in count.items()]
#     heapq.heapify(heap)
#     return [heapq.heappop(heap)[1] for _ in range(k)]