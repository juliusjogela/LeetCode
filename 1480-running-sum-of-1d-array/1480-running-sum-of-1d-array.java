class Solution {
    public int[] runningSum(int[] nums) {    //nums = 1,2,3,4
    int[] runningSum = new int[nums.length];
    runningSum[0] = nums[0];              //      0,1,2,3
        for(int i = 1; i<nums.length; i++)
        {                                     //i=0 nrunning = 1,
         runningSum[i] = runningSum[i-1] + nums[i];
        }
    return runningSum;
    }
}