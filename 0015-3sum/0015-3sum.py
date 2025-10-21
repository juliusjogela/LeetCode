class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            leftIndex = i + 1
            rightIndex = len(nums) - 1
            
            while leftIndex < rightIndex:
                total = nums[i] + nums[leftIndex] + nums[rightIndex]
                
                if total == 0:
                    res.append([nums[i], nums[leftIndex], nums[rightIndex]])
                    
                    # Skip duplicates for left pointer
                    while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex + 1]:
                        leftIndex += 1
                    
                    # Skip duplicates for right pointer
                    while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex - 1]:
                        rightIndex -= 1
                    
                    # Move both pointers
                    leftIndex += 1
                    rightIndex -= 1
                    
                elif total < 0:
                    leftIndex += 1
                else:
                    rightIndex -= 1
        
        return res
                

