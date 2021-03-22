class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, height, right) for left, right, height in buildings]
        events += [(right, 0, 0) for _, right, _ in buildings]

        events.sort(key = lambda x: (x[0], -x[1], x[2]))
        
        hq = [(0, float("inf"))]  
        
        res = [[0, 0]]
        for left, height, right in events:
            if height != 0:
                heappush(hq, (-height, right))

            while hq[0][1] <= left:
                heappop(hq)

            if res[-1][1] != -hq[0][0]:
                res.append([left, -hq[0][0]])
                
        return res[1:]