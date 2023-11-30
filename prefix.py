nums = [0,-1,-1,-1,-1,-1]
n = len(nums)
prefix = [0] * n
prefix[0] = nums[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + nums[i]
print (prefix)