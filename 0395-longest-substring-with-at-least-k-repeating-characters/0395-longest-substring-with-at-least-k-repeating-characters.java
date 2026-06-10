class Solution {
    public int longestSubstringHelper(String s, int start, int end, int k){
        if(end - start < k){
            return 0;
        }

        int[] freq = new int[26];

        for(int i = start; i < end; i++){
            freq[s.charAt(i) - 'a']++;
        }

        // Check if all chars are valid
        boolean allValid = true;
        for(int i = 0; i < 26; i++){
            if(freq[i] > 0 && freq[i] < k){
                allValid = false;
                break;
            }
        }

        if(allValid){
            return end - start;
        }

        int max = 0, segmentStart = start;

        for(int i = start; i < end; i++){
            if(freq[s.charAt(i) - 'a'] < k){
                max = Math.max(max, longestSubstringHelper(s, segmentStart, i, k));
                segmentStart = i+1;
            }
        }
        
        //last segment
        return Math.max(max, longestSubstringHelper(s, segmentStart, end, k));
    }

    public int longestSubstring(String s, int k) {
        return longestSubstringHelper(s, 0, s.length(), k);
    }
}

// TC: O(n^2) for each character in the string we can have a split, and in each split we will go till n characters
// SC: O(n) recursion depth
// Approach: find freq of each char in string, now scan left to right, when you see a char with freq < k, it means this can never be part of the answer. So split the string and check whether split string satisfies the conditions
