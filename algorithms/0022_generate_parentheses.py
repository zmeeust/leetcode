"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(')')
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = 3
    assert solution.generateParenthesis(n) == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    n = 1
    assert solution.generateParenthesis(n) == ["()"]
