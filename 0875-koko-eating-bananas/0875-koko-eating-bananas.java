class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int n = piles.length;
        int low = 1, high = 0;
        for(int pile : piles) high = Math.max(high, pile);

        int ans = high;
        while(low <= high){
            int mid = low + (high - low)/2;
            // System.out.println("mid "+mid);
            int time = 0;
            for(int i = 0; i < n; i++){
                time += Math.ceil((double)piles[i]/mid);
            }
            if(time <= h){
                ans = mid;
                high = mid - 1;
            } 
            else{
                low = mid + 1;
            }
            // System.out.println("time "+time);
            // System.out.println("ans "+ans);
        }
        return ans;
    }
}

// TC: O(log(high)*n)
// SC: O(1)
// Approach: The answer will lie between min and max pile values. We will use binary search to guess the k value, if time is less than equals h then ans is valid. If time is greater than h, then we can increase the k.