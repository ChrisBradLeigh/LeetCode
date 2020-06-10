class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0
        for x in range(len(nums)):
            if nums[x] == target:
                return x
            else:
                if target > nums[x]:
                    position = x+1
        return(position)
