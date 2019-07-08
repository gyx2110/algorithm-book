import random
x = random.randint(1,7)
y = random.randint(8,16)
s = random.randint(3,7)
nums = [_ for _ in range(1,x+1)]+ [_ for _ in range(y,y+s)][::-1]
print nums
l = 0
r = len(nums)-1

while l < r:
    m = (l+r)/2
    if nums[r] > nums[m]:
        r = m - 1
    elif nums[l] < nums[m]:
        l = m + 1
print nums[l]
