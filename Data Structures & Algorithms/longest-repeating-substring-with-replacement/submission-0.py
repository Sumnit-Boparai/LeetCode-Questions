class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)
        mainLetterCount = 0
        l = 0
        for r, letter in enumerate(s):
            count[letter] += 1
            mainLetterCount = max(count[letter], mainLetterCount)

            while (r - l + 1) - mainLetterCount > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res