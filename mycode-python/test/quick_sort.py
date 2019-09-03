def partition(nums,l,r):
    p = nums[l]
    i = l
    j = r
    while i<j:
        while j>i and nums[j] >= p:
            j-=1
        nums[i] = nums[j]
        while i<j and nums[i] < p:
            i+=1
        nums[j] = nums[i]
    nums[i] = p
    return i
def quick_sort(nums,l,r):
    if(l<r):
        p = partition(nums,l,r)
        quick_sort(nums,l,p-1)
        quick_sort(nums,p+1,r)
nums = [5,1,7]
l = len(nums)
quick_sort(nums,0,l-1)
print nums