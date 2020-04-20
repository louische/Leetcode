class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        def help(needle: str) -> []:
            res = [0] * len(needle)
            j = 0
            i = 1
            while(i < len(needle)):
                if(needle[i] == needle[j]):
                    res[i] = j + 1
                    j += 1
                else:
                    while(j > 0 and needle[i] != needle[j]):
                        j = res[j - 1] 
                        if needle[i] == needle[j]:
                            res[i] = j + 1
                            j += 1
                            break
                i += 1  
            return res

        arr = help(needle)
        print(arr)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] != needle[j]:
                if j > 0:
                    j = arr[j - 1]
                else:
                    i += 1
            else:
                i += 1
                j += 1
            if j == len(needle):
                return i - j 
        return  -1

