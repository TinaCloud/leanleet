class Solution(object):
    def maxValue(self, n, index, maxSum):
        
        def check(mid, m):
            if m >= mid:
                return mid*(mid+1)//2 + m - mid
            else:
                return (mid*2 - m + 1)*m//2
        left = 0
        right =  maxSum+1
        while left < right:
            mid = (left + right) // 2
            if check(mid, index+1) + check(mid, n-index) - mid > maxSum:
                right = mid
            else:
                left = mid + 1
        return left - 1









    