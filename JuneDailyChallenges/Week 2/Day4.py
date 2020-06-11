class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countColours = [0, 0, 0]
        for x in range(len(nums)):
            if nums[x] == 0:
                countColours[0] += 1
            elif nums[x] == 1:
                countColours[1] += 1
            elif nums[x] == 2:
                countColours[2] += 1
        tracker = 0
        for y in range(3):
            for z in range(countColours[y]):
                nums[tracker] = y
                tracker +=1
