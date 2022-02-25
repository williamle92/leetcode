'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        
        return [left, right]
        
        
#    helper function to do the actual binary search
#   left bias is going to be a boolean
#   if true, it will point the r pointer to the left of middle and check to see if the new middle is the target, if so then it will be the new index
#    if false, it will do the opposite but to the right side
    def binarySearch(self, nums, target, leftBias):
        left, right = 0, len(nums) -1
#         we set -1 because the function says to return -1 if it is not found
        index = -1
        while left <= right:
#           middle will set to the middle which is sum of left and right floor division
            middle = (left + right)// 2
    
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
#                 if the middle is equal to the target, then we set index = to middle
                index = middle
                if leftBias:
#             we are going to check the left side now to see if it is equal to the target, if so it will run one more time and set the new index equal to the left most
                    right = middle - 1
#                 we are going to do the same with the right side now, check to see if there is a right most value that matches the target. (remember r + r//2 m will equal the r pointer, if it is equal to the target then)
                else:
                    left = middle + 1
        return index