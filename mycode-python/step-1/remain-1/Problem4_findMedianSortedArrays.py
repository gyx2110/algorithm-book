class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        MAX = 0x3fffffff
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                max_of_left = max(-MAX if i==0 else A[i-1], -MAX if j==0 else B[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left
                min_of_right = min(MAX if i==m else A[i],MAX if j==n else B[j])
                return (max_of_left + min_of_right) / 2.0