class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sLetters = defaultdict(int)
        tLetters = defaultdict(int)

        for i in range(len(s)):
            sLetters[s[i]] += 1
            tLetters[t[i]] += 1
        
        return sLetters == tLetters