from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        e = 1/1000000
        def helper(cards):
            n = len(cards)
            if n == 1:
                if abs(cards[0] - 24) <= e:
                    return True
                return False

            for i in range(n):
                for j in range(i+1, n):
                    a, b = cards[i], cards[j]
                    poss = []
                    poss.append(a+b)
                    poss.append(a*b)
                    poss.append(a-b)
                    poss.append(b-a)
                    if abs(b) > 0:
                        poss.append(a/b)
                    if abs(a) > 0:
                        poss.append(b/a)

                    rest = []
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        rest.append(cards[k])

                    for p in poss:
                        if helper(rest+[p]):
                            return True
            return False

        return helper(cards)

        # TC: O(n^3)
        # SC: O(n)
        # Approach: we can apply all possible combinations between all pairs and reduce cards length. FInally when cards length is 1, check if number stored is 24
        

        