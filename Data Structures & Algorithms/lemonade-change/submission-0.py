class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        till = {5:0, 10:0, 20:0}

        def getChange(change, denomonation):
            
            while change >= denomonation and till[denomonation] > 0:
                change -= denomonation
                till[denomonation] -= 1
            return change
        
        for bill in bills:
            till[bill] += 1
            change = bill - 5

            change = getChange(change, 20)
            change = getChange(change, 10)
            change = getChange(change, 5)
            
            if change != 0:
                return False
        return True