'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

from collections import Counter
class Solution:
    def containsDuplicate(self, nums) :
        seen = Counter(nums)
        for value in seen.values():
            if value > 1:
                return True
        return False

class Solution:
    def containsDuplicate(self, nums) :
        sorted_nums = sorted(nums)
        for i in range(len(nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))