class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def find_div(rem, d):
            res = []
            seen = dict()
            while rem != 0:
                rem *= 10
                m = rem // d
                if rem in seen:
                    res.append(")")
                    idx = seen[rem]
                    res.insert(idx, "(")
                    break
                idx = len(res)
                seen[rem] = idx
                res.append(str(m))
                rem = rem%d
            return ''.join(res)

        if numerator == 0:
            return '0'
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        print(sign)
        n, d = abs(numerator), abs(denominator)
        s1 = sign+str(n// d)
        rem = n % d
        if rem == 0:
            return s1
        s2 = find_div(rem, d)
        return s1+"."+s2
        