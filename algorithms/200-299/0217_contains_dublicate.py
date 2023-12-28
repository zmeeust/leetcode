""""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numb = set()
        for number in nums:
            if number in numb:
                return True
            numb.add(number)
        return False


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums) is True

    nums = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums) is False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums) is True
