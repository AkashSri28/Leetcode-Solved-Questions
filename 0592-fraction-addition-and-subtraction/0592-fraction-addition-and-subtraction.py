class Solution:
    def fractionAddition(self, expression: str) -> str:
        i, curr_num, curr_deno = 0, 0, 1
        
        # Parse the expression to find all fractions
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        isNeg = False
        for frac in fractions:
            parts = frac.split('/')
            num, deno = int(parts[0]), int(parts[1])
            
            curr_num = curr_num*deno + num*curr_deno
            curr_deno = curr_deno*deno
            
        gcd = math.gcd(curr_num, curr_deno)
        curr_num //= gcd
        curr_deno //= gcd
        return str(curr_num)+"/"+str(curr_deno)