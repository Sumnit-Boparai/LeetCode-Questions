class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            letter = columnNumber % 26

            res.append(chr(65 + letter))
            columnNumber //= 26
        
        return "".join(reversed(res))