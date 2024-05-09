class Solution:
    def isPalindrome(self, x: int) -> bool:
        strg = str(x)
        rev = len(strg) - 1
        for index in range(len(strg)):
            if strg[rev] == strg[index]:
                rev -= 1
            else:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
        