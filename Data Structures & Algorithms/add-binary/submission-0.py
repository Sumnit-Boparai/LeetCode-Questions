class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        pA, pB = len(a) - 1, len(b) - 1
        
        while carry or pA >= 0 or pB >= 0:
            bitA = int(a[pA]) if pA >= 0 else 0
            bitB = int(b[pB]) if pB >= 0 else 0

            total = bitA + bitB + carry
            bit = total % 2
            carry = total // 2

            res.append(str(bit))
            pA -= 1
            pB -= 1
        return "".join(reversed(res))
