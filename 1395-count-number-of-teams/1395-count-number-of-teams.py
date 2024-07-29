class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count, n = 0, len(rating)
        
        for i in range(1, n-1):
            left_smaller = left_larger = right_smaller = right_larger = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left_smaller += 1
                if rating[j] > rating[i]:
                    left_larger += 1    
                
            for j in range(i+1, n):
                if rating[j] < rating[i]:
                    right_smaller += 1
                if rating[j] > rating[i]:
                    right_larger += 1   
                
            count += left_smaller*right_larger + left_larger*right_smaller
            
        return count
        