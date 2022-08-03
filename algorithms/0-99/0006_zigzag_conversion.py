"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        # res = ''
        # for r in range(num_rows):
        #     increment = 2 * (num_rows - 1)
        #     for i in range(r, len(s), increment):
        #         res += s[i]
        #         if r > 0 and r < num_rows - 1 and i + increment - 2 * r < len(s):
        #             res += s[i + increment - 2 * r]
        #
        # return res

        # Create your list of rows based on numRow Amount
        rows = [''] * num_rows
        index, increment = 0, 1
        for char in s:
            rows[index] += char
            # here we say if numRow reached max row decrement
            if index == num_rows - 1: increment = -1
            # here we say if numRow at the start increment it
            if index == 0: increment = 1
            # here we apply either the increment or decrement based of if statement
            index += increment
        return ''.join(rows)


if __name__ == '__main__':
    solution = Solution()

    s = 'PAYPALISHIRING'
    num_rows = 3
    assert solution.convert(s, num_rows) == 'PAHNAPLSIIGYIR'

    s = 'PAYPALISHIRING'
    num_rows = 4
    assert solution.convert(s, num_rows) == 'PINALSIGYAHRPI'

    s = 'A'
    num_rows = 1
    assert solution.convert(s, num_rows) == 'A'
