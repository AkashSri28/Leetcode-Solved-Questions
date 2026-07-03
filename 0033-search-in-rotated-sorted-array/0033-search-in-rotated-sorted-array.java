class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        int ans = -1;
        while(low <= high){
            int mid = low + (high - low)/ 2;
            // System.out.println(mid);
            if(nums[mid] == target) return mid;
            // check if left half is sorted
            else if(nums[low] <= nums[mid]){
                if(nums[low] <= target && target < nums[mid]){
                    high = mid - 1;
                }
                else{
                    low = mid + 1;
                }
            }
            // else right half is sorted
            else{
                if(nums[high] >= target && target > nums[mid]){
                    low = mid + 1;
                }
                else{
                    high = mid - 1;
                }
            }
        }
        return ans;
    }
}