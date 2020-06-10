def prefixCompare(str1, str2):
    res = ""
    for x in range(len(str1)):
        if x < len(str2):
            if str1[x] == str2[x]:
                res+=str1[x]
            else:
                return(res)
    return(res)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return("")
        prefix = strs[0]
        for x in range(len(strs)):
            prefix = prefixCompare(prefix, strs[x])
        return prefix
