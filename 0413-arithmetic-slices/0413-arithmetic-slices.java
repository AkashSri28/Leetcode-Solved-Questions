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

        return ans;
    }
}

// TC: O(n)
// SC: O(1)
// Approach: For each index, check if it forms valid triplet. If breaks, reset counter.