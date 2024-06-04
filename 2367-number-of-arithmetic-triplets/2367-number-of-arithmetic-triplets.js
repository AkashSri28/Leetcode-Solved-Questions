/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    let count = 0, j=1;
    for(let i=0;i<nums.length-2;i++){
        while(j< nums.length && nums[j] - nums[i] < diff){
            j++;
        }
        if(nums[j] - nums[i] == diff){
            for(let k=0;k<nums.length;k++){
                if(nums[k] - nums[j] == diff){
                    count = count+1;
                    break;
                }
            }
        }
    }
    return count;
};