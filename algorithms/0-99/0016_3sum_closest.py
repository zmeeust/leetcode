"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = 1000000000000
        nums.sort()

        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i - 1] and i > 0:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                if abs(target - summ) < abs(target - closest):
                    closest = summ
                if summ <= target:
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1
                else:
                    r -= 1
        return closest


if __name__ == '__main__':
    solution = Solution()

    nums = [-1, 2, 1, -4]
    target = 1
    assert solution.threeSumClosest(nums, target) == 2

    nums = [0, 0, 0]
    target = 1
    assert solution.threeSumClosest(nums, target) == 0

    nums = [-13, 592, -501, 770, -952, -675, 322, -829, -246, 657, 608, 485, -112, 967, -30, 182, -969,
            559, -286, -64, 24, 365, -158, 701, 535, -429, -217, 28, 948, -114, -536, -711, 693, 23, -958,
            -283, -700, -672, 311, 314, -712, -594, -351, 658, 747, 949, 70, 888, 166, 495, 244, -380, -654,
            454, -281, -811, -168, -839, -106, 877, -216, 523, -234, -8, 289, -175, 920, -237, -791, -976,
            -509, -4, -3, 298, -190, 194, -328, 265, 150, 210, 285, -176, -646, -465, -97, -107, 668, 892, 612,
            -54, -272, -910, 557, -212, -930, -198, 38, -365, -729, -410, 932, 4, -565, -329, -456, 224, 443,
            -529, -428, -294, 191, 229, 112, -867, -163, -979, 236, -227, -388, -209, 984, 188, -549, 970, 951,
            -119, -146, 801, -554, 564, -769, 334, -819, -356, -724, -219, 527, -405, -27, -759, 722, -774, 758,
            394, 146, 517, 870, -208, 742, -782, 336, -364, -558, -417, 663, -914, 536, 293, -818, 847, -322, 408,
            876, -823, 827, 167]
    target = 7175
    assert solution.threeSumClosest(nums, target) == 2921
