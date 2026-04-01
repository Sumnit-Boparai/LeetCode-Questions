class Solution:
    def isHappy(self, n: int) -> bool:
        itterations = set()
        currNum = n

        while currNum not in itterations:
            itterations.add(currNum)

            if currNum == 1:
                return True
            
            newNum = 0
            for digit in str(currNum):
                newNum += int(digit) ** 2
            currNum = newNum
        
        return False