"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curt_str):
            if len(curt_str) == len(digits):
                res.append(curt_str)
                return
            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, curt_str + c)

        if digits:
            backtrack(0, "")

        return res


if __name__ == '__main__':
    solution = Solution()

    digits = "23"
    assert solution.letterCombinations(digits) == ["ad", "ae", "af", "bd",
                                                   "be", "bf", "cd", "ce", "cf"]

    digits = ""
    assert solution.letterCombinations(digits) == []

    digits = "2"
    assert solution.letterCombinations(digits) == ["a", "b", "c"]
