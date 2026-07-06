class Solution {
    /**
     * @param {number[]} nums
     * @return {string}
     */
    largestNumber(nums) {
        let arr = nums.map(String);
        arr.sort((a,b)=>(b+a)-(a+b));
        let res = arr.join("");
        if(res[0]=='0')
            return "0";
        return res;
    }
}
