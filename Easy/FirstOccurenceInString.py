class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1
        else:
            for start in range(len(haystack) - len(needle) + 1):
                if needle == haystack[start:(start+len(needle))]:
                    break
                else:
                    continue
        return start



sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("mississippi", "issip"))