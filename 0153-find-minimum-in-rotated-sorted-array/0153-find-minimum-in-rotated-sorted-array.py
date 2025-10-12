class Solution(object):
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        lo = 0
        hi = len(nums) -1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[0] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

    
        