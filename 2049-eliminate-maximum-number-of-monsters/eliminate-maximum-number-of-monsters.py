class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        steps = []
        for i in range(len(dist)):
            steps.append(ceil(dist[i] / speed[i]))
        
        steps.sort()
        res = 0
        for monster_time in steps:
            if res >= monster_time:
                return res
            res += 1
        return res
