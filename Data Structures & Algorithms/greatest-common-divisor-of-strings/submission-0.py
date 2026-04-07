class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def checkDivisor(divisor, string) -> bool:
            start = 0
            while start < len(string):
                if string[start:start+len(divisor)] != divisor:
                    return False
                start += len(divisor)
            return True
        
        res = ""
        
        for i in range(1, len(str1)+1):
            if len(str1) % (i) != 0 or len(str2) % (i) != 0:
                continue
            
            divisor = str1[:i]
            if checkDivisor(divisor, str1) and checkDivisor(divisor, str2):
                res = divisor
        
        return res
        

            