class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        area = 0
        rects = [item for x1, y1, x2, y2 in rectangles for item in [[x1, y1, y2, 0], [x2, y1, y2, 1]]]
        last = rects[0][0]
        heap = [(float('inf'), float('inf'))]
        for x, y1, y2, k in sorted(rects):
            h = start = end = 0
            for m, n in heap:
                if m > end:
                    h += end - start
                    start, end = m, n
                else:
                    end = max(end, n)
            area += (x-last)*h
            import bisect
            heap.remove((y1, y2)) if k else bisect.insort(heap, (y1, y2))
            last = x

        return area % (10**9 + 7)
    