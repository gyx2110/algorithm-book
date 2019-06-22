# class Solution:
#     def findDuplicate(self, nums):
#         n = -1
#         while nums[0] != pre:
#             n = nums[0]
#             self.swap(nums,n)
#         return nums[0]
#     def swap(self, nums,n):
#         nums[0] = nums[n]
#         nums[n] = n
class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return slow
        # return slow
if __name__ == "__main__":
    s = Solution()
    print s.findDuplicate([1,3,4,2,2])