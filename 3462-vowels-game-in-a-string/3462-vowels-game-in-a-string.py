class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        for ch in s:
            if ch in vowels:
                return True
        return False

        # TC: O(n)
        # SC: O(1)
        # Approach: basically alice will take max possible vowels in first turn. So if there are odd number of vowels, alice will take everything in first turn, then bob will have nothing to pick, alice wins. if there are even vowels, alice will take total - 1 vowels, bob cant pick 1 vowel, hence alice wins again. 
        # Only case when bob can win is when there are no vowels, alice will have no move. So check if there is any vowel in string, return True, else false