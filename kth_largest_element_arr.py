'''
215. Kth Largest Element in an Array
Medium

8386

465

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# cheat solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#         k is going to be the length of the list - k e.g. 1 will be -1
        k = len(nums) - k
        
        def quickSelect(l,r):
# all numbers before the anchor will be less than the compare point, and will switch place with the numbers at the index i(while looping) and the anchor. The anchor will always be a number higher than your comparison number. 
            largestNumAnchor, compareNum = l, nums[r]
            for i in range(l,r):
#             if the number at current index is less than the comparison number, we switch place with the anchor, therefore anchor is always largest number
                if nums[i] <= compareNum:
                    nums[i], nums[largestNumAnchor] = nums[largestNumAnchor], nums[i]
                    largestNumAnchor += 1
# now we switch place of the largest number anchor with the comparison num
            nums[largestNumAnchor], nums[r] = nums[r], nums[largestNumAnchor]
#             if the anchor is currently less than k( remember these are both indexes), than we run quickselect on the right half
            if largestNumAnchor < k: return quickSelect(largestNumAnchor + 1, r)
#     if the anchor is larger than the k, then we have to run it on the left half
            elif largestNumAnchor > k: return quickSelect(l, largestNumAnchor -1)
#     return the number is it matches the correct index
            else: return nums[largestNumAnchor]
        return quickSelect(0, len(nums) -1)
