class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        left = 0
        right = len(nums) - 1
         
        while left <= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                left = left + 1
                right = right -1 
            
        return -1

            
