from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newting = sorted(nums)
        secondp = len(newting)-1
        index = 0
        index2 = 0
        
        dictionary = {}
        for x in nums:
            if x in dictionary:
                dictionary[x].append(index2)
                index2 += 1
            else:
                dictionary[x] = [index2]
                index2 += 1
                
        while index != len(newting)-1:
            sum = newting[index] + newting[secondp]
            if sum == target:
                return [dictionary[newting[index]].pop(0), dictionary[newting[secondp]].pop(0)]
            elif sum > target:
                secondp -= 1
            else:
                index += 1

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))



