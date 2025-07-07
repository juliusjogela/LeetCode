class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary(row, target):
            n = len(row)
            low = 0
            high = n-1
            while low <= high:
                mid = low + (high-low) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    low = mid+1
                else:
                    high = mid - 1
            return False
        
        for i in range(len(matrix)):
            if binary(matrix[i], target):
                return True
        return False
        