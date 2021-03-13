class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            max_start = max(A[i][0], B[j][0])
            min_end = min(A[i][1], B[j][1])
            if max_start <= min_end:
                res.append([max_start, min_end])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
                
        return res
    
    