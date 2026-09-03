from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
                continue

            right = stack.pop()
            left = stack.pop()

            if tok == "+":
                stack.append(left + right)
            elif tok == "-":
                stack.append(left - right)
            elif tok == "*":
                stack.append(left * right)
            else:
                # Division truncated toward zero
                quotient = abs(left) // abs(right)

                if (left < 0) != (right < 0):
                    quotient = -quotient

                stack.append(quotient)

        return stack[-1]