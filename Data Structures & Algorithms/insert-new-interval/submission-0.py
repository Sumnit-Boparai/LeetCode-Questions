class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start > newEnd:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            elif end < newStart:
                res.append(intervals[i])
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        res.append([newStart, newEnd])
        return res