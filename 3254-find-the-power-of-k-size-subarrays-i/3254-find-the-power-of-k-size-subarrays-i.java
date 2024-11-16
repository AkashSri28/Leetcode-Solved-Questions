class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;

        // Edge case: if k > n or nums is empty
        if (k > n || nums == null || nums.length == 0) {
            return new int[0];
        }

        int[] res = new int[n - k + 1];
        int consecutiveCount = 0, resultIndex = 0;

        // Initialize the sliding window
        for (int i = 1; i < k; i++) {
            if (isConsecutive(nums[i - 1], nums[i])) {
                consecutiveCount++;
            }
        }

        // Check the first window
        res[resultIndex++] = (consecutiveCount == k - 1) ? nums[k - 1] : -1;

        // Sliding window
        int left = 0, right = k;
        while (right < n) {
            // Update the consecutive count for the sliding window
            if (isConsecutive(nums[left], nums[left + 1])) {
                consecutiveCount--;
            }
            if (isConsecutive(nums[right - 1], nums[right])) {
                consecutiveCount++;
            }

            // Add result for the current window
            res[resultIndex++] = (consecutiveCount == k - 1) ? nums[right] : -1;

            // Move the window
            left++;
            right++;
        }

        return res;
    }

    // Helper function to check if two numbers are consecutive
    private boolean isConsecutive(int a, int b) {
        return b == a + 1;
    }
}