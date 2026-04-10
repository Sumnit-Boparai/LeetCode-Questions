class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + '#' + word)

        return "".join(res)
    
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            i = j+1
            res.append(s[i:i+size])
            i += size
        return res




