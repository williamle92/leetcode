"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Examples:
Input: s = "()"
Output: true
Input: s = "()[]{}"
Output: true
Input: s = "(]"
Output: false

"""
def valid(string):
    arr = []
    for letter in string:
        if arr and (letter == ")" and arr[-1] == "("):
            arr.pop()
        elif arr and (letter == "}" and arr[-1] == "{"):
            arr.pop()
        elif arr and (letter == "]" and arr[-1] == "["):
            arr.pop()
        else:
            arr.append(letter)
    return len(arr) == 0

print(valid("()[]{}"))
print(valid("(])"))
print(valid("([)]"))
# print(valid("()[]{}"))


# Solution 2
class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(", "}":"{", "]":"["}
        arr = []
        for char in s:
            if arr and (char in map and map[char] == arr[-1]):
                arr.pop()
            else:
                arr.append(char)
        return len(arr) == 0
