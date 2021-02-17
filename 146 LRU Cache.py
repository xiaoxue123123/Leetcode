
# 网上的答案
import collections
def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    v = self.dic.pop(key)
    self.dic[key] = v   # set key as the newest one
    return v

def set(self, key, value):
    if key in self.dic:
        self.dic.pop(key)
    else:
        if self.remain > 0:
            self.remain -= 1
        else:  # self.dic is full
            self.dic.popitem(last=False)
    self.dic[key] = value















# 自己写的， 但是落在了recency要是一个集合，不能只是一个value。
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            self.recency = key
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            self.dict[key] = value
        else:
            if len(self.dict) == 1 and self.capacity == 1:
                self.dict = {}
            if len(self.dict) == self.capacity and self.capacity != 1:
                for k, v in self.dict.items():
                    if k != self.recency:
                        to_delete = k
                        break
                del self.dict[to_delete]
            self.dict[key] = value
        self.recency = key


obj = LRUCache(2)
obj.get(2)
obj.put(2,6)
obj.get(1)
obj.put(1,5)
obj.put(1,2)
obj.get(1)
obj.get(2)

for k,v in obj.dict.items():
    print(k,v)