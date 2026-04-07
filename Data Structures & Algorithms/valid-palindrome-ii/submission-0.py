class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(str, l, r):
            while l <= r:
                if str[l] != str[r]:
                    return (l, r)
                l += 1
                r -= 1
            return (l, r)

        l, r = checkPalindrome(s, 0, len(s)-1)
        if l < r:
            l1, r1 = checkPalindrome(s, l+1, r)
            l2, r2 = checkPalindrome(s, l, r-1)
            return (l1 >=  r1) or (l2 >= r2)
        return True