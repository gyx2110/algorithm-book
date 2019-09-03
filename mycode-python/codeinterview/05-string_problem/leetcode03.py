class Solution:
    def lengthOfLongestSubstring(self, s):
        L = res = 0
        map = {}
        for R in range(len(s)):
            if s[R] in map and L <= map[s[R]]:
                L = map[s[R]] + 1
            else:
                res = max(res, R - L + 1)
            map[s[R]] = R
        return res
if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")