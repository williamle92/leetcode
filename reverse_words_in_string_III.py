"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        left, right = 0,0
        for index, value in enumerate(arr):
            if value == " ":
                right = index -1
                self.reverser(arr, left, right)
                left = index + 1
                
            if index == len(arr) -1:
                right = index
                self.reverser(arr, left, right)
                
        return "".join(arr)
    
    
    def reverser(self, word, left, right):
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return word