class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s.lower() if char.isalnum())

        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True