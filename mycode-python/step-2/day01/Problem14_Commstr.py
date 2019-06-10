class Solution(object):
    def longestCommonPrefix(self, strs):
        size = len(strs)
        if size <= 1:
            return strs[0] if size == 1 else '' 
        res = ''
        for c in range(len(strs[0])):
            isSame = True
            for i in range(1,len(strs)):
                if c >= len(strs[i]) or strs[i][c] != strs[0][c]:
                    isSame = False
                    break
            if isSame:
                res+=strs[0][c]
            else:
                return res
        return res
if __name__ == "__main__":
    print Solution().longestCommonPrefix(['aca','cba'])