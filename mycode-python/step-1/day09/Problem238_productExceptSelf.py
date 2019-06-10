class Solution(object):
    def productExceptSelf(self, nums):
        l = [nums[0]] * len(nums)
        r = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            l[i] = nums[i] * l[i-1]
            r[-i-1] = nums[-i-1]*r[-i]
        res = [0] * len(nums)
        for i in range(1, len(nums)-1):
            res[i] = l[i-1] * r[i+1]
        res[0] = r[1]
        res[-1] = l[-2]
        return res
