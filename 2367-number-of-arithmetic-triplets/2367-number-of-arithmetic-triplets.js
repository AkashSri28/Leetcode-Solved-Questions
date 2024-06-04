/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    let count = 0;
  const numSet = new Set(nums); // To quickly check the existence of a number

  for (let i = 0; i < nums.length; i++) {
    const num1 = nums[i];
    const num2 = num1 + diff;
    const num3 = num2 + diff;

    if (numSet.has(num2) && numSet.has(num3)) {
      count++;
    }
  }

  return count;
};