"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in parentheses:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


if __name__ == '__main__':
    solution = Solution()

    s = "()"
    assert solution.isValid(s) is True

    s = "()[]{}"
    assert solution.isValid(s) is True

    s = "(]"
    assert solution.isValid(s) is False
