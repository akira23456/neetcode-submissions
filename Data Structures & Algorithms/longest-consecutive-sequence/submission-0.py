class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        max_count = 1
        count = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:                
                temp = nums[i-1]
                if nums[i] == temp + 1:
                    count = count + 1
                elif nums[i] == temp:
                    continue
                else:
                    count = 1
                max_count = max(max_count, count)
        
        return max_count