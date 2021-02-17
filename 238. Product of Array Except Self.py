nums = [1,2,3,4]


# solution 1: 把i左边和i右边的数的乘积都存在array里面

#
# left = [0]*len(nums)
# right = [0]*len(nums)
#
# left[0] = right[-1] = 1
# left[1] = nums[0]
# right[-2] = nums[-1]

# for i in range(2,len(nums)):
#     left[i] = left[i-1]*nums[i-1]
#     right[-i-1] = right[-i]*nums[-i]
#
# prod = []
# for i in range(len(nums)):
#     prod.append(left[i]*right[i])

#print(prod)

# solution 2: 只存左边的乘积，右边的乘积用一个variable 代替

left = [0]*(len(nums))
left[0]=1
left[1]=nums[0]
prod = [0]*(len(nums))
for i in range(2,len(nums)):
    left[i] = left[i-1]*nums[i-1]

right = 1
# 从右到左计算right prod
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1:
        prod[i] = 1*left[-1]
    elif i == len(nums)-2:
        right = right * nums[-1]
        prod[i]=nums[-1]*left[-2]
    else:
        right = right*nums[i+1]
        prod[i]=right*left[i]