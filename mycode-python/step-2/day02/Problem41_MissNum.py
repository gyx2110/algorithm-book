class Solution(object):
    def firstMissingPositive(self, nums):
        l,r = 0,len(nums)
        while l<r:
            if nums[l]==l+1:
                l+=1
            elif nums[l]<=l or nums[l]>r or nums[nums[l] -1]==nums[l]:
                r-=1
                nums[l] = nums[r]
            else:
                t=nums[nums[l]-1]
                nums[nums[l]-1] = nums[l] 
                nums[l] = t
        return l+1
if __name__ == "__main__":
    s = Solution()
    print s.firstMissingPositive([2,1])