class Solution {
    public int[] twoSum(int[] nums, int target) {
        int attempt = 0;
        for(int i = 0; i< nums.length; i++)
        {
          for(int j = 0; j< nums.length; j++)
          {
            if(i == j)
            {}
            else
            {
            attempt = nums[i] + nums[j];
            if(attempt == target)
            return new int[] {i, j};
            }
          }
        }
        return nums;
    }
}