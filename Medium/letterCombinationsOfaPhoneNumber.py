from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        final = []
        def backtrack(i, combination):
            if len(digits) == len(combination):
                final.append(combination)
                return
            for char in phone[int(digits[i])]:
                backtrack(i + 1, combination + char)
        backtrack(0, "")
        return final





        





        