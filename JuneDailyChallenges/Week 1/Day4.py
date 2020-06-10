class Solution:
    def reverseString(self, s: List[str]) -> None:
        for x in range(int(len(s)/2)):
            temp = s[x]
            s[x] = s[len(s)-1-x]
            s[len(s)-1-x] = temp
