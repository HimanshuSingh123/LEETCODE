from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        newflowerbed = [0] + flowerbed + [0]
        for i in range(1, len(newflowerbed) - 1):
            if (newflowerbed[i - 1] == 0) and (newflowerbed[i] == 0) and (newflowerbed[i+1] == 0):
                newflowerbed[i] = i
                count += 1
        if count >= n: # >= because count can exceed number of n specified
            return True
        return False
    
sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,1], 2))
print(sol.canPlaceFlowers([1,0,0,0,0,0,1], 2))