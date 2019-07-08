# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         return self.helper(s, wordDict, {})
        
#     def helper(self, s, wordDict, memo):
#         if s in memo: return memo[s]
#         if not s: return []
        
#         res = []
#         for word in wordDict:
#             if not s.startswith(word):
#                 continue
#             #如果当前串的长度刚好和字典中的某个串相等
#             if len(word) == len(s):
#                 res.append(word)
#             #如果不等，则递归解决剩余的部分
#             else:
#                 resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
#                 print len(resultOfTheRest)
#                 #每一个item都是一种以word开头可能的拆分方案
#                 for item in resultOfTheRest:
#                     item = word + ' ' + item
#                     res.append(item)
#                     #如果当前串的长度刚好和字典中的某个串相等
#         memo[s] = res
#         return res

class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, map):
        if s in map: return map[s]
        if not s: return ['']
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            #递归解决剩余的部分
            #每一个item都是一种以word开头可能的拆分方案
            for item in self.dfs(s[len(word):], wordDict, map):
                item = word + ('' if item =='' else ' ') + item
                res.append(item)
        map[s] = res
        return res
if __name__ == "__main__":
    s = Solution()
    print s.wordBreak("catsanddog",["cat","cats","and","sand","dog"])