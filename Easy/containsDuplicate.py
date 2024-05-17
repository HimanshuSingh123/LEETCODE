from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for i, n in enumerate(nums):
            if n in mapp:
                return True
            else:
                mapp[n] = i
        return False
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))