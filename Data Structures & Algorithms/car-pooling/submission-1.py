class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        schedule = defaultdict(int)
        start, end = 1001, 0
        for passengers, on, off in trips:
            schedule[on] += passengers
            schedule[off] -= passengers
            start = min(start, on)
            end = max(end, off)
        
        total = 0
        i = start
        
        while i <= end:
            total += schedule.pop(i, 0)
            
            if total > capacity:
                return False

            i += 1
        
        return True
