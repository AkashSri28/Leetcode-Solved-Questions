class Solution {
    public int splitArray(int[] nums, int k) {
        long low = 0, high = 0;
        for (int n : nums) {
            high += n;       
            if (n > low) {  
                low = n;
            }
        }

        long ans = high;
        while(low <= high) {
            long mid = low + (high - low)/2;
            long curr = 0;
            int cnt = 0;
            for(int i = 0; i < nums.length; i++){
                if(curr + nums[i] <= mid){
                    curr += nums[i];
                }
                else{
                    cnt++;
                    curr = nums[i];
                }
            }
            if(cnt <= k-1){
                ans = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return (int)ans;
    }
}