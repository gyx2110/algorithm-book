def part(nums):
    pivot = nums[0]
    left = -1
    right = len(nums)
    i = 0
    while i<right:
        if nums[i]<pivot:
            left+=1
            swap(nums,left,i)
            i+=1
        elif nums[i]==pivot:
            i+=1
        else:
            right-=1
            swap(nums,i,right)
def swap(nums,i,j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t
nums = [4,7,1,4,2,3,10,8]
part(nums)
print nums
