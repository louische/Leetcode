class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
    
        res = [0] * (len(needle) + 1)
        j = -1
        i = 0
        res[0] = -1
        while(i < len(needle)):
            while(j >= 0 and needle[i] != needle[j]):
                j = res[j]
            i += 1
            j += 1
            res[i] = j

        i = 0
        j = 0
        while(i < len(haystack)):
            while(j >= 0 and needle[j] != haystack[i]):
                j = res[j]
            i += 1
            j += 1
            if j == len(needle):
                return i - len(needle)
        return -1
