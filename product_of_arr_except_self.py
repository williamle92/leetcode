'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

class Solution:
    def productExceptSelf(self, nums):
        # create a new array with None values equal to length of list, we are doing this so we can insert a value to an array at a certain index... will give an error if index does not exist
#       keep in mind that it is not len(nums) -1 because we want to create an array with the exact number of values in an arr. So if an array has 6 values, and it is 0-5 in an array, but it is
#       still 6 values therefore when we create a new arr with 6 values, it will be 0-5
        arr = [None] * len(nums)
#       Create a product variable to track the product before current index
        product = 1
#       since the first value is not counted towards the products before, we can first add the product and then multiply the product at its current index
        for i in range(len(nums)):
            arr[i] = product
            product *= nums[i]
#       Now we are doing the reverse, we are going backwards and then multiplying each value in the arr by the product other than itself
        product = 1
#     remember range always stop before the end value, thats why it is negative 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= product
            product *= nums[i]
            
        return arr
            