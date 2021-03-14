class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left, right, i = [], [], 0
        
        for i, item in enumerate(intervals):
            if item[1] < newInterval[0]: 
                left.append(item)          
            elif item[0] > newInterval[1]: 
                right = intervals[i:]
                break
            else: 
                newInterval[0] = min(newInterval[0], item[0])
                newInterval[1] = max(newInterval[1], item[1]) 
        return left + [newInterval] + right