class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num = i
            bits = 0
            while num > 0:
                bits += 1 if num & 1 else 0
                num >>= 1
            res.append(bits)
        return res