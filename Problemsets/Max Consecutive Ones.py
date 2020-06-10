class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        y = 0
        ones = []
        for x in range(len(nums)):
            if nums[x] != 0:
                y+=1
            else:
                ones.append(y)
                y = 0
        ones.append(y)
        ones.sort()
        print(ones)
        if len(ones) < 2:
            return(ones[0])
        else:
            return(ones[-1])
