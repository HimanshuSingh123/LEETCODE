from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandi = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxCandi:
                candies[i] = True
            else:
                candies[i] = False
        return candies
    
sol = Solution()
print(sol.kidsWithCandies([12,1,12], 10))
print(sol.kidsWithCandies([4,2,1,1,2], 1))
print(sol.kidsWithCandies([2,3,5,1,3], 3))