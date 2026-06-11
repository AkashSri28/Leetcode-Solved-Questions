class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int left = 0;
        int ans = 0;
        while(left <= nums.length - 3){
            int right = left + 1;
            int diff = nums[right] - nums[left];
            int count = 0;
            while(right < nums.length && nums[right] - nums[right-1] == diff){
                if(right-left+1 >= 3){
                    count++;
                    ans += count;
                }
                right++;
            }
            left = right-1;
        }
        return ans;
    }
}