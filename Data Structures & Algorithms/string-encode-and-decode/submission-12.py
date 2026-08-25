from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Edge case: empty input
        if len(strs) == 0:
            return ""
        
        # Encode with "*" as separator and add a trailing "*" to mark the end
        string = strs[0]
        for i in range(1, len(strs)):
            string = string + '~' + strs[i]
        string = string + '~'   # always add a trailing * so decode knows the split
        return string

    def decode(self, s: str) -> List[str]:
        # Edge case: empty string input
        if s == "":
            return []

        myList = []
        string = ""

        for i in range(len(s)):
            if s[i] == "~":
                myList.append(string)
                string = ""
            else:
                string += s[i]

        # If string didn’t end with "*", append leftover
        if string != "":
            myList.append(string)

        return myList
