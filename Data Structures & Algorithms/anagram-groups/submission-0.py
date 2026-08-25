from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # key -> list of words

        for word in strs:
            # Sort the word and use it as key
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())