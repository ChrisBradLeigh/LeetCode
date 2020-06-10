class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = len(nums) -1
        x = 0
        while x < counter:
            if nums[x] == nums[x+1]:
                nums.remove(nums[x])
                counter -= 1
                x -= 1
            x += 1
        return(len(nums))
    
