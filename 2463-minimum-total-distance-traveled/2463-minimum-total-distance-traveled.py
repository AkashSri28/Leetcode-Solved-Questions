class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        all_factory = []
        for pos, freq in factory:
            while freq:
                all_factory.append(pos)
                freq -= 1
                
        all_factory.sort()
        
        len_robot = len(robot)
        len_factory = len(all_factory)
        
        dp = [[-1]*len_factory for _ in range(len_robot)]
        
        def repair(r, f):
            if r < 0:
                return 0
            if f < 0:
                return float('inf')
            
            if dp[r][f] == -1:
                exclude = repair(r, f-1)
                include = abs(robot[r] - all_factory[f]) + repair(r-1, f-1)
                dp[r][f] = min(exclude, include)
                
            return dp[r][f]        
        
        return repair(len_robot-1, len_factory-1)
        
                    
        
                
                        
        
        