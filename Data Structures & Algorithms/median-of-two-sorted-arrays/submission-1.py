class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr3 = sorted(nums1 + nums2)

        left = 0
        right = len(arr3)

        if len(arr3) % 2 == 0: 
            mid = (left + right) // 2 
            
            final = (arr3[mid - 1] + arr3[mid]) / 2.0
            return final
        else:
            mid = (left + right) // 2
            return float(arr3[mid])