class Solution(object):
    # def wiggleSort(self, nums):
    #     tmp = [_ for _ in nums]
    #     tmp.sort()
    #     l = (len(tmp)-1)/2
    #     h = len(tmp)-1
    #     for i in range(len(tmp)):
    #         if i%2:
    #             nums[i] = tmp[h]
    #             h-=1
    #         else:
    #             nums[i] = tmp[l]
    #             l-=1
    def wiggleSort(self, nums):
            tmp = [_ for _ in nums]
            tmp.sort()
            n = len(tmp)
            l = (n-1)/2
            h = n-1
            k = l
            i = 0
            while i<n:
                if l>-1:
                    nums[i] = tmp[l]
                    i,l = i+1,l-1
                if h>k:
                    nums[i] = tmp[h]
                    i,h = i+1,h-1
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,1,2,1]
    s.wiggleSort(nums)
    print nums
