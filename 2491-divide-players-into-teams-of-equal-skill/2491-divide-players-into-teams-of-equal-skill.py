class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chem = 0
        n = len(skill)//2
        sk = sum(skill)//n
        
        skill.sort()
        
        if sk*n != sum(skill):
            return -1
        
        i, j = 0, len(skill)-1
        
        while i<j:
            if skill[i] + skill[j] != sk:
                return -1
            chem += (skill[i]*skill[j])
            i += 1
            j -= 1
            
        return chem
            
        
        
        