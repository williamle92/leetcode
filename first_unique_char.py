"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                d[char] = i
                seen.add(char)
            elif char in d:
                del d[char]
        
        return min(d.values()) if d else -1



s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))