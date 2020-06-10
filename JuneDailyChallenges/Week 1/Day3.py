def diff(l):
    if l[0] > l[1]:
        return l[0] - l[1]
    else:
        return l[1] - l[0]
    
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for x in range(len(costs)):
            for y in range(x+1, len(costs)):
                if diff(costs[x]) < diff(costs[y]):
                    temp = costs[x]
                    costs[x] = costs[y]
                    costs[y] = temp
        citya = 0
        cityb = 0
        total = 0
        for each in costs:
            if (each[0] <= each[1] and citya < len(costs)/2) or cityb == len(costs)/2:
                total += each[0]
                citya+=1
            else:
                total += each[1]
                cityb+=1
        return(total)
