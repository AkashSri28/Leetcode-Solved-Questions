/**
 * @param {string} s
 * @return {number}
 Approach: Use two pointer to find a subarray with no repeating elements, as element gets repeated move left pointer until duplicate element is no longer included in subarray. Use set to remember seen elements.
 TC= O(n)
 SC= O(n)
 */
var lengthOfLongestSubstring = function(s) {
    const set= new Set();
    var result= 0, j= 0;
    for(let i=0; i<s.length; i++){
        while(set.has(s[i])){
            set.delete(s[j]);
            j++;
        }
        set.add(s[i]);
        result= Math.max(result, set.size);
    }
    return result;
};