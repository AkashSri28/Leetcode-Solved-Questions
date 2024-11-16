class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n-k+1];
        int cnt = 0, index = 0;
        
        for(int i=1;i<k;i++){
            if(nums[i] == nums[i-1]+1){
                cnt += 1;
            }
        }
        if(cnt == k-1){
            res[index++] = nums[k-1];
        }
        else{
            res[index++] = -1;
        }
        
        int i=0, j=k;
        while(j<n){
            if(nums[i] == nums[i+1]-1){
                cnt -= 1;
            }
            if(nums[j] == nums[j-1]+1){
                cnt += 1;
            }
            if(cnt == k-1){
                res[index++] = nums[j];
            }
            else{
                res[index++] = -1;
            }
            i += 1;
            j += 1;
        }
        
        return res;
    }
}