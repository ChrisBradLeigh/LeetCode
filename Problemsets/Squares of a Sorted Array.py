class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        output = []
        for each in A:
            output.append(pow(each, 2))
        output.sort()
        return(output)
