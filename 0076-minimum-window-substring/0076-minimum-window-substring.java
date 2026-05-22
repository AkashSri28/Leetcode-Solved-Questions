class Solution {
    public String minWindow(String s, String t) {
        if(s == null || t == null || s.length() < t.length()){
            return "";
        }
        int l = 0;

        Map<Character, Integer> need = new HashMap<>();
        for(char c:t.toCharArray()){
            need.put(c, need.getOrDefault(c, 0) + 1);
        }
        int need_len = need.size();
        
        Map<Character, Integer> seen = new HashMap<>();
        int seen_len = 0;
        int ans_len = Integer.MAX_VALUE;
        int ans_left = 0;
        int ans_right = 0;

        for(int r = 0; r<s.length(); r++){
            char c = s.charAt(r);
            seen.put(c, seen.getOrDefault(c, 0) + 1);

            if(need.containsKey(c) && seen.get(c).equals(need.get(c))){
                seen_len++;
            }

            while(seen_len == need_len){
                if(r-l+1 < ans_len){
                    ans_len = r-l+1;
                    ans_left = l;
                    ans_right = r;
                }
                char ch = s.charAt(l);
                seen.put(ch, seen.get(ch) - 1);
                if(need.containsKey(ch) && seen.get(ch) < need.get(ch)){
                    seen_len--;
                }
                l++;
            }
        }
        if(ans_len == Integer.MAX_VALUE){
            return "";
        }
        return s.substring(ans_left, ans_right+1);

    }
}