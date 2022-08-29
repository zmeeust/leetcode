"""
You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order.
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

Constraints:
1 <= nums.length <= 100
1 <= nums[i], target <= 100
"""


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()

        def bin_search(arr, t, lower=True):
            left, right = 0, len(arr) - 1

            while left <= right:

                mid = (left + right) // 2

                if arr[mid] == t:
                    if lower:
                        if mid == left or nums[mid] != arr[mid - 1]:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == right or arr[mid] != arr[mid + 1]:
                            return mid
                        else:
                            left = mid + 1

                elif arr[mid] > t:
                    right = mid - 1
                elif nums[mid] < t:
                    left = mid + 1

            return -1

        start, end = bin_search(nums, target), bin_search(nums, target, False)

        if start < 0 and end < 0:
            return []

        return list(range(start, end + 1))


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 5, 2, 3]
    target = 2
    assert solution.targetIndices(nums, target) == [1, 2]

    nums = [1, 2, 5, 2, 3]
    target = 3
    assert solution.targetIndices(nums, target) == [3]

    nums = [1, 2, 5, 2, 3]
    target = 5
    assert solution.targetIndices(nums, target) == [4]

    nums = [1, 2, 5, 2, 3]
    target = 4
    assert solution.targetIndices(nums, target) == []

    nums = [11, 80, 25, 75, 62, 57, 98, 91, 72, 19, 41, 85, 48, 58, 5, 43, 47, 97, 45, 89, 45]
    target = 35
    assert solution.targetIndices(nums, target) == []

    nums = [95, 59, 19, 25, 49, 44, 85, 59, 14, 59, 2, 58, 70, 36, 43, 81, 84, 77, 43, 16, 99, 60]
    target = 27
    assert solution.targetIndices(nums, target) == []
