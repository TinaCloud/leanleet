class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        min_ans=1
        max_ans=(position[-1]-position[0])//(m-1)

        def check(length,position,m):
            count=1
            i=0
            for j in range(1,len(position)):
                if position[j]-position[i]>=length:
                    count+=1
                    i=j
            return count>=m 
        
        left=min_ans
        right=max_ans
        ans=0

        while(left<=right):
            mid=left+(right-left)//2
            if check(mid,position,m):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans







    