class Solution {
    public int longestSubstringHelper(String s, int start, int end, int k){
        if(start == end){
            return 0;
        }
        int[] freq = new int[26];
        int totalChar = 0, validChar = 0;

        for(int i = start; i < end; i++){
            if(freq[s.charAt(i) - 'a'] == 0){
                totalChar++;
            }
            freq[s.charAt(i) - 'a']++;
            if(freq[s.charAt(i) - 'a'] == k){
                validChar++;
            }
        }

        if(totalChar == validChar){
            return end - start;
        }

        for(int i = start; i < end; i++){
            if(freq[s.charAt(i) - 'a'] < k){
                return Math.max(longestSubstringHelper(s, start, i, k), longestSubstringHelper(s, i+1, end, k));
            }
        }
        return 0;
    }

    public int longestSubstring(String s, int k) {
        return longestSubstringHelper(s, 0, s.length(), k);
    }
}