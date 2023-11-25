out = []
nums = [2,3,5]      
for i in range(len(nums)):
    resulti = 0
    for j in range(len(nums)):
        resulti += abs(nums[i]- nums[j])
    out.append(resulti)
print (out)