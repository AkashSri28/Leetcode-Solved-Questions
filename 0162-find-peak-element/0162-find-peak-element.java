class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        int low = 0, high = n - 1;
        while(low <= high){
            int mid = low + (high - low)/ 2;
            if(mid - 1 == -1 || nums[mid - 1] < nums[mid]){
                if(mid + 1 == n || nums[mid+1] < nums[mid]){
                    return mid;
                }
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return -1;
    }
}