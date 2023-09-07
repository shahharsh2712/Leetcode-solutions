class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = {}
        t_count = {}
        
        for i in s:
            if i in s_count:
                s_count[i] += 1
            else:
                s_count[i] = 1
                
        for i in t:
            if i in t_count:
                t_count[i] += 1
            else:
                t_count[i] = 1
                
        steps = 0
        for i in s_count:
            diff = s_count.get(i, 0) - t_count.get(i, 0)
            if diff > 0:
                steps += diff
            
        return steps