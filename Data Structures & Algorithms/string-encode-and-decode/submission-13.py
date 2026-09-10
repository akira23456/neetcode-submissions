from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            if len(word) >= 2:
                word = word[-1] + word[1:-1] + word[0]

            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            word = s[start:start + length]

            # Swap the first and last characters back
            if len(word) >= 2:
                word = word[-1] + word[1:-1] + word[0]

            decoded.append(word)
            i = start + length

        return decoded