class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3) return 0;

        int count = 0;
        int ans = 0;

        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
                count++;        // one more new slice added
                ans += count;   // all slices ending at i
            } else {
                count = 0;      // streak broken, reset
            }
        }
        
        // int left = 0;
        // int ans = 0;
        // while(left <= nums.length - 3){
        //     int right = left + 1;
        //     int diff = nums[right] - nums[left];
        //     int count = 0;
        //     while(right < nums.length && nums[right] - nums[right-1] == diff){
        //         if(right-left+1 >= 3){
        //             count++;
        //             ans += count;
        //         }
        //         right++;
        //     }
        //     left = right-1;
        // }
        return ans;
    }
}