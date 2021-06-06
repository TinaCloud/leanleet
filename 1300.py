class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        summ = sum(arr)
        if summ<=target:
            return max(arr)
        l = len(arr)
        val = target//l
        summ,last = 0,0
        while summ<target:
            last = summ
            summ = 0
            for i in range(l):
                summ +=arr[i] if val>arr[i] else val
            val +=1
        return val-2 if abs(target-summ)>=abs(target-last) else val-1







    