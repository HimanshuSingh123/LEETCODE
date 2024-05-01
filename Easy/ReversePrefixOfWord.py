class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            print("yeah that word " + ch + " aint even in here")
            return word
        else:
            index = word.index(ch) + 1
            firstPart = word[:index]
            secondPart = word[index:]
            rev = firstPart[::-1]
            combined = rev + secondPart
            return combined

sol = Solution()
print(sol.reversePrefix("abcdefd", "d"))
print(sol.reversePrefix("xyxzxe", "z"))
print(sol.reversePrefix("abcd", "z"))
