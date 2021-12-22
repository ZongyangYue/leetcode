class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the min element is both smaller than the left and the right
        #edge case 1: min at the rightmost, smaller than the left
        #edge case 2: min at the leftmost, smaller than its right and the rightmost
        #binary search
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            
            #for edge case 1
            if mid == len(nums) - 1:
                if nums[mid] < nums[mid-1] and nums[mid] < nums[0]:
                    return nums[mid]
            
            #this line includes the edge case 2 since nums[-1] is the right most
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
        
        return nums[left]
