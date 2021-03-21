class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        coordinates = set()
        area = 0
        for rec in rectangles:
            bottom_left = (rec[0], rec[1])
            bottom_right = (rec[0], rec[3])
            top_left = (rec[2], rec[1])
            top_right = (rec[2], rec[3])
            
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            
            for coord in [bottom_left, bottom_right, top_left, top_right]:
                if coord not in coordinates:
                    coordinates.add(coord)
                else:
                    coordinates.remove(coord)
        
        if len(coordinates) != 4:  
            return False      

        bottom_left = sorted(coordinates)[0]    
        top_right = sorted(coordinates)[3]
        return area == (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])   