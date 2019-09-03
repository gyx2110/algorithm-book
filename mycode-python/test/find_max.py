def _max(nums,i):
    if i==len(nums)-1:
        return nums[-1]
    return max(_max(nums,i+1),nums[i])
print _max([3,2,5,1,8,2,0],0)
