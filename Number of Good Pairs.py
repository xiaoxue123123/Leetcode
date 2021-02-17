nums = [1,2,3,1,1,3]


def numIdenticalPairs(nums):
    pairs = 0
    l = len(nums)
    for i in range(l):
        for j in range(l):
            if i < j and nums[i] == nums[j]:
                pairs += 1
    return pairs

def numIdenticalPairs(nums):
    from math import factorial
    from collections import Counter

    def nCr(n,r):
        if n<r: return 0
        else: return (factorial(n)/(factorial(r)*factorial(n-r)))

    counter=Counter(nums)
    freq = counter.values()
    return(int(sum([nCr(x,2) for x in list(freq)])))