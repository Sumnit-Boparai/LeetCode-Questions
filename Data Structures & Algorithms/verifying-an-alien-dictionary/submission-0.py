class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        orderMap = {}
        for i, letter in enumerate(order):
            orderMap[letter] = i

        for i in range(1, len(words)):
            l1, l2 = 0, 0
            word1, word2 = words[i-1], words[i]
            
            while l1 < len(word1) and l2 < len(word2):
                if orderMap[word1[l1]] > orderMap[word2[l2]]:
                    return False
                elif orderMap[word1[l1]] < orderMap[word2[l2]]:
                    break
                else:
                    l1 += 1
                    l2 += 1

            if (l1 == len(word1) or l2 == len(word2)) and (len(word1) > len(word2)):
                return False
        return True