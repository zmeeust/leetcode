"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the
32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1,
then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        constraint = 2147483647
        sign = -1 if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        output = 0

        while dividend >= divisor:
            tmp = divisor
            mul = 1
            while dividend >= tmp:
                dividend -= tmp
                output += mul
                mul += mul
                tmp += tmp

        output = -output if sign < 0 else output

        return min(constraint, max(-constraint - 1, output))


if __name__ == '__main__':
    solution = Solution()

    dividend = 10
    divisor = 3
    assert solution.divide(dividend, divisor) == 3

    dividend = 7
    divisor = -3
    assert solution.divide(dividend, divisor) == -2

    dividend = -2147483648
    divisor = 1
    assert solution.divide(dividend, divisor) == -2147483648

    dividend = -2147483648
    divisor = -1
    assert solution.divide(dividend, divisor) == 2147483647
