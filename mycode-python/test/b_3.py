#coding=utf-8
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    W = int(sys.stdin.readline().strip())
    w = map(int,sys.stdin.readline().strip().split(' '))
    v = map(int,sys.stdin.readline().strip().split(' '))
    dp = [0]*(W+1)
    for i in range(w[0],W+1):
        dp[i] = v[0]
    for i in range(1,len(w)):
        for j in range(W,w[i]-1,-1):
            dp[j] = max(dp[j],dp[j-w[i]]+v[i])    
    print dp[W]
# 		for (int i = 1; i < w.length; i++) {
# 			for (int j = W; j >= w[i]; j--) {
# 				dp[j] = Math.max(dp[j], dp[j - w[i]] + v[i]);
# 			}
# 		}
# 		return dp[W];