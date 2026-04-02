class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getAnagram(word) -> tuple:
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return tuple(res)
        
        res = defaultdict(list)
        for word in strs:
            res[getAnagram(word)].append(word)

        return list(res.values())