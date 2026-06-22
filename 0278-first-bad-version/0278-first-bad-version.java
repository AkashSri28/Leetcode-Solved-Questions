/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int low = 1, high = n, mid;
        while(low <= high){
            mid = low + (high - low)/2;
            if(isBadVersion(mid)){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return low;
    }
}

// TC: O(logn)
// SC: O(1)
// Approach: check between 1 and n versions, whenever we get a bad version we will mark it and remove search space from its right as they all will be bad anyways.