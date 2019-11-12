#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


	# public static int coinsOther(int[] arr, int aim) {
	# 	if (arr == null || arr.length == 0 || aim < 0) {
	# 		return 0;
	# 	}
	# 	return processOther(arr, arr.length - 1, aim);
	# }
	# //递归函数的功能是求arr[0..index]组成aim的方法数
	# public static int processOther(int[] arr, int index, int aim) {
	# 	int res = 0;
	# 	if (index == -1) {
	# 		res = aim == 0 ? 1 : 0;
	# 	} else {
	# 		for (int i = 0; arr[index] * i <= aim; i++) {
	# 		 //用0,1,2..i张arr[index],
	# 		 //递归求以arr[0..index-1]组成aim - arr[index] * i的方法数
	# 			res += processOther(arr, index - 1, aim - arr[index] * i);
	# 		}
	# 	}
	# 	return res;
	# }
if __name__ == "__main__":
    def dfs(nums,n,k):
        if n==1:
            return True
        elif k==len(nums):
            return n==1
        else:
            i=0
            while n/nums[k]>=1:
                if dfs(nums,n/(nums[k]*i),k):
                    return True
                i+=1
            dfs(nums,n/(nums[k]*i),k)

    n = int(sys.stdin.readline().strip())
    nums = map(int,sys.stdin.readline().strip().split(' '))
    print dfs(nums,n,0)
    while l<len(s) and r<len(s):
        if num<n:
            num+=ord(s[r])-ord('a')+1
            r+=1
        elif num==n:
            num-=ord(s[l])-ord('a')+1
            ans = max(ans,r-l)
            l+=1
        elif num>n:
            num-=ord(s[l])-ord('a')+1
            l+=1
    print ans
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = map(int, line.split())
    #     for v in values:
    #         ans += v
    # print ans