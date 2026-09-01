class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):

            if i == 0:
                past = nums[i]
            elif past == nums[i]:
                return True
            else:
                past = nums[i]

        return False


