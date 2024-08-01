class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        def find_age(f, s):
            return int(f)*10+int(s)
        
        for detail in details:
            if find_age(detail[11], detail[12]) > 60:
                count += 1
        return count
        