class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if length ==0:
            return length
        i,j=0,0
        w = []
        res = 0
        left,right = 0,0
        while i<length and j<length:
            if s[j] in w:
                w.remove(s[i])
                i+=1
            else:
                w.append(s[j])
                j+=1
                if j-i > res:
                    left = i
                    right= j
                    res = j-i
        return s[left:right]
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         length = len(s)
#         if length ==0:
#             return length
#         map = {}
#         l,res = 0,0
#         for r in range(length):
#             if s[r] in map:
#                 l = max(map[s[r]],l)
#             res = max(res,r-l+1)
#             map[s[r]] = r+1
#         return res
if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring('abcabcbb')
