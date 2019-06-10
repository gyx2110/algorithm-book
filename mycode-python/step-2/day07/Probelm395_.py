class Solution(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if len(s)<k:
                return 0
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
if __name__ == "__main__":
    s = Solution()
    print s.longestSubstring('weitong',2)