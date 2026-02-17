"""
Problem: Running Sum of 1D Array
LeetCode: https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: Easy

Approach:
Traverse the array and keep adding the previous sum.
Each position stores cumulative total.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        sum = 0
        for num in nums:
            sum += num
            runningSum.append(sum)
        return runningSum 
            

# TEST
assert Solution().runningSum([1,2,3,4]) == [1,3,6,10]
assert Solution().runningSum([1,1,1,1]) == [1,2,3,4]
assert Solution().runningSum([3,1,2,10,1]) == [3,4,6,16,17]
print("1480 passed ✅")