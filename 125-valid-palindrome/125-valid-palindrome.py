class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        regex = re.compile('[^a-zA-Z0-9]')
        pal = regex.sub('', s)
        rev_pal = pal[::-1]
        if pal == rev_pal:
            return True
        else:
            return False