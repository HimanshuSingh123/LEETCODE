from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []
        i = 1
        while i <= n:
            if ((i % 3 == 0) and (i % 5 ==0)):
                array.append("FizzBuzz")
            elif i % 3 == 0:
                array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(i))
            i += 1
        return array

sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(10))
print(sol.fizzBuzz(15))

