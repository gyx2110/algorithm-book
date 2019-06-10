class Solution(object):
    def removeDuplicates(self, nums):
        i,j = 0,1
        while j<len(nums):
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
        return i+1
if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([1,1])