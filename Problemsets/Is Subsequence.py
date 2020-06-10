class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        substr = ""
        if s == "":
            return True
        try:
            for x in range(len(t)):
                if t[x] == s[counter]:
                    counter += 1
                    substr += t[x]
        except:
            print(substr)
        if substr == s:
            return True
        else:
            return False
