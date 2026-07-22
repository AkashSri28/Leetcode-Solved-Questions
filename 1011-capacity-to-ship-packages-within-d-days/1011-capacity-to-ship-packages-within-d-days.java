class Solution {
    public int shipWithinDays(int[] weights, int days) {
        long low = 1, high = 0;
        for (int w : weights) {
            high += w;       
            if (w > low) {  
                low = w;
            }
        }
        long ans = high;
        // System.out.println(low+" "+high);
        while(low <= high){
            long mid = low + (high - low)/2;
            long load = 0;
            int count = 0;
            for(int i =0; i < weights.length; i++){
                if(load + weights[i] <= mid){
                    load += weights[i];
                }
                else{
                    count++;
                    load = weights[i];
                }
            }
            count++;
            if(count <= days){
                ans = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return (int)ans;
    }
}

// TC: O(n*log(high - low))
// SC: O(1)
// Approach: Ship should carry minimum weight greater than equal to highest weight on belt. 
// Max capacity will be sum of all weights then everything will be carried in 1 day
// Now ans will be between these 2