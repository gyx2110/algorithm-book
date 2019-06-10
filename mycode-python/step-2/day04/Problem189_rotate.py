class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        k%=l
        while k:
            k-=1
            tmp = nums[-1]
            i = l-1
            while i>0:
                nums[i] = nums[i-1]
                i-=1
            nums[0] = tmp
        return nums
if __name__ == "__main__":
    s = Solution()
    print s.rotate([1,2,3,4,5],4)