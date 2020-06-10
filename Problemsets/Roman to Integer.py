class Solution:
    def romanToInt(self, s: str) -> int:
        s+="E"
        total = 0
        for x in range(len(s)-1):
            if s[x] == 'I' and (s[x+1] != 'V' and s[x+1] != 'X'):
                total+=1
            elif s[x] == 'I' and (s[x+1] == 'V' or s[x+1] == 'X'):
                total-=1
            elif s[x] == 'V':
                total+=5
            elif s[x] == 'X' and (s[x+1] != 'L' and s[x+1] != 'C'):
                total+=10
            elif s[x] == 'X' and (s[x+1] == 'L' or s[x+1] == 'C'):
                total-=10
            elif s[x] == 'L':
                total+=50
            elif s[x] == 'C' and (s[x+1] != 'D' and s[x+1] != 'M'):
                total+=100
            elif s[x] == 'C' and (s[x+1] == 'D' or s[x+1] == 'M'):
                total-=100
            elif s[x] == 'D':
                total+=500
            elif s[x] == 'M':
                total+=1000
            elif s[x] == 'E':
                break;
        return total
