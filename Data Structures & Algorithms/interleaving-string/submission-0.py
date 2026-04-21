class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = [False] * (len(s1)+1)
        cache[0] = True

        for r in range(len(s2)+1):
            print(cache)
            for c in range(len(s1)+1):
                letter = r + c - 1

                if (r > 0 and cache[c] and s2[r-1] == s3[letter]) or (c > 0 and cache[c-1] and s1[c-1] == s3[letter]) or (r == 0 and c == 0):
                    cache[c] = True
                else:
                    cache[c] = False
        return cache[-1]