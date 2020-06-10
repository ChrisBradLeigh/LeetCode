class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for each in nums:
            if len(str(each))%2==0:
                counter+=1
        return(counter)
