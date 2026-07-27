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

// TC: O(n*log sum(nums) + n)
// SC: O(1)
// Approach: we will check for valid splits
// if the number of valid splits is less than k-1, means this answer is valid. We can decrease mid to check if cnt still fit in k-1
// else our splits are more we need to increase low