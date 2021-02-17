nums = [9,6,4,2,3,5,7,0,1]

# solution 1.space complexity O(1)
m = max(nums)
def missingNumber(nums):
    m = len(nums)
    for i in range(m + 1):
        if i not in nums:
            return (i)
missingNumber(nums)



import time

start = time.time()
missingNumber(nums)
end = time.time()
time_n1 = end - start
print(time_n1)



def missingNumber2(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)
import time

start = time.time()
missingNumber2(nums)
end = time.time()
time_n2 = end - start
print(time_n2)

def missingNumber3(nums):
    return sum(range(len(nums) + 1)) - sum(nums)


start = time.time()
missingNumber3(nums)
end = time.time()
time_n3 = end - start
print(time_n3)