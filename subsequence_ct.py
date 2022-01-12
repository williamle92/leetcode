"""
Given two non-empty arrays of integers(numbers), write a function that 
determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren’t necessarily 
adjacent in the array but that are in the same order as they appear in 
the array. For instance, the numbers [1,3,4] form a subsequence of the 
array [1,2,3,4], and so do the numbers [2,4]. Note that a single number 
in an array and the array itself are both valid subsequences of the array.
( [1],[2],[3],[4]and [1,2,3,4] are all valid subsequences of [1,2,3,4] )
Sample Output
array = [5,1,22,25,6,-1,8,10]
subsequence = [1,6,-1,10]
Answer: True

"""

def validSubSeq(arr, seq):
    for i in seq:
        if i not in arr:
            return False
    return True
        



print(validSubSeq([5,1,22,25,6,-1,8,10],[1,6,-1,10]))