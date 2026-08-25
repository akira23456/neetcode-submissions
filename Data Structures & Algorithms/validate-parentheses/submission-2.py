class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack or stack.pop() != mapping[s[i]]:
                    return False

        if not stack:
            return True
        else:
            return False