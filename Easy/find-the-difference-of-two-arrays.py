from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        mapped = [[],[]]
        nums1, nums2 = set(nums1), set(nums2)
        for i in nums1:
            if i not in nums2:
                mapped[0].append(i)
        for i in nums2:
            if i not in nums1:
                mapped[1].append(i)
        return mapped
            
sol = Solution()
print(sol.findDifference([1,2,3], [2,4,6]))
print(sol.findDifference([1,2,3,3], [1,1,2,2]))
        
        