"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution(object):
    def myAtoi(self, s):
        # Remove any additional spaces before the given string
        s = s.lstrip()

        # If string is empty return 0
        if len(s) == 0:
            return 0

        # String index from where the processing should start
        start = 0

        # Handling numbers with +/- sign
        sign_multiplier = 1
        if s[0] == '-':  # Handling for negative sign numbers
            sign_multiplier = -1
            start = 1
        elif s[0] == '+':  # Handling for signed positive sign number
            start = 1

        result = 0

        index = start
        while index < len(s):
            # Handling for non numeric values
            if not ('0' <= s[index] <= '9'):
                return result * sign_multiplier

            # Calculate the result for current iteration
            result = result * 10 + ord(s[index]) - ord('0')

            # Check if result exceeds MinInt32 or MaxInt32
            min_int_32 = 2 ** 31
            if result * sign_multiplier <= -min_int_32:
                return -min_int_32
            elif result * sign_multiplier >= min_int_32 - 1:
                return min_int_32 - 1
            index += 1

        return result * sign_multiplier


if __name__ == '__main__':
    solution = Solution()

    x = '42'
    assert solution.myAtoi(x) == 42

    x = '   -42'
    assert solution.myAtoi(x) == -42

    x = '4193 with words'
    assert solution.myAtoi(x) == 4193
