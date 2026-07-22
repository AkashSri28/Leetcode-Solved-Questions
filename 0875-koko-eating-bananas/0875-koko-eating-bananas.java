class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1, high = 0;
        for(int pile : piles) high = Math.max(high, pile);

        int ans = high;
        while(low <= high){
            int mid = low + (high - low)/2;
            int time = 0;
            for(int pile : piles){
                time += Math.ceil((double)pile/mid);
            }
            if(time <= h){
                ans = mid;
                high = mid - 1;
            } 
            else{
                low = mid + 1;
            }
        }
        return ans;
    }
}

// TC: O(log(high)*n)
// SC: O(1)
// Approach: The answer will lie between min and max pile values. We will use binary search to guess the k value, if time is less than equals h then ans is valid. If time is greater than h, then we can increase the k.