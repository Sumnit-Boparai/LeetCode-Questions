class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cache = defaultdict(int)
        start = 10 ** 9 + 1
        end = 0

        for card in hand:
            cache[card] += 1
            start = min(start, card)
            end = max(end, card)

        i = start
        while i <= end:
            if cache[i] == 0:
                i += 1
            else:
                for j in range(i, i + groupSize):
                    if cache[j] == 0:
                        return False
                    cache[j] -= 1
        return True