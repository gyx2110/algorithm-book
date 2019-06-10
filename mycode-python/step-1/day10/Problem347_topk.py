import heapq
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         count = {}
#         for num in nums:
#             count[num] = count.get(num,0)+1
#         heap = []
#         for key,v in count.items():
#             heap.append((-v,key))
#         heapq.heapify(heap)
#         res = []
#         for i in range(k):
#             #必须用heappop函数，底层用的是列表存的堆结构
#             res.append(heapq.heappop(heap)[1])        
#         return res
class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        c = Counter(nums)
        listRes = c.most_common(k)
        res = []
        for item in listRes:
            res.append(item[0])
        return res
if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent([2,3,4,1,4,0,4,-1,-2,-1],2)

