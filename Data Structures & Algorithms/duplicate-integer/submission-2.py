class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) < 1:
            return False
        else:
            current = nums[0]
        for i in range(1,len(nums)):
            
            if nums[i] == current:
                return True
            else:
                current = nums[i]
        
        return False

