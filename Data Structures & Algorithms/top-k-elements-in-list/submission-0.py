from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1

        # Sort keys by frequency, descending
        sorted_keys = sorted(dictionary, key=lambda x: dictionary[x], reverse=True)
        return sorted_keys[:k]