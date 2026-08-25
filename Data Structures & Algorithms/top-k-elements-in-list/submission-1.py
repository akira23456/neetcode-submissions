from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}

        for num in nums:
            diction[num] = diction.get(num, 0) + 1

        result = []
        
        for _ in range(k):
            max_count = -1
            most_frequent_num = None
            
            for num, count in diction.items():
                if count > max_count:
                    max_count = count
                    most_frequent_num = num
            
            result.append(most_frequent_num)
            
            del diction[most_frequent_num]

        return result