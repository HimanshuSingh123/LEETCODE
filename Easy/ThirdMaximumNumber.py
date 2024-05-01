from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        original = list(set(nums))
        originalcopy = original.copy()
        listLen = len(original)
        maxcount = 0
        while listLen != 0:
            if len(originalcopy) < 3:
                return max(originalcopy)
            elif (listLen) == 1 or (maxcount == 2):
                return max(original)
            else:
                remove = max(original)
                original.remove(remove)
                listLen -= 1
                maxcount += 1

sol = Solution()
print(sol.thirdMax([2,2,3,1]))
print(sol.thirdMax([1,2]))
print(sol.thirdMax([3,2,1]))
print(sol.thirdMax([1,2,2,5,3,5]))



