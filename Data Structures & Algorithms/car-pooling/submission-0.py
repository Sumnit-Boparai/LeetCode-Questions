class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        schedule = defaultdict(int)

        for passengers, start, end in trips:
            schedule[start] += passengers
            schedule[end] -= passengers
        
        total = 0
        i = 0
        
        while schedule:
            total += schedule.pop(i, 0)
            
            if total > capacity:
                return False

            i += 1
        
        return True
