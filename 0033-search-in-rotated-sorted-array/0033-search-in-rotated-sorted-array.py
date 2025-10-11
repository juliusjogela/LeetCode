class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        pivot = findPivot(nums, 0, n-1)
        if nums[pivot] == target:
            return pivot
        if pivot == 0:
            return binarySearch(nums, 0, n-1, target)
        if nums[0] <= target:
            return binarySearch(nums, 0, pivot-1, target)
        return binarySearch(nums, pivot+1, n-1, target)
        
def binarySearch(nums, lo, hi, target):
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid +1
            else:
                hi = mid-1
        return -1
    
def findPivot(nums, lo, hi):
        while lo <hi:
            if nums[lo] <= nums[hi]:
                return lo
            mid = (lo+hi) //2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        return lo
