class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i]==nums[j]:
                    count += 1
                j += 1
            i += 1
        return count
                    
# TEST
assert Solution().numIdenticalPairs([1,2,3,1,1,3]) == 4
assert Solution().numIdenticalPairs([1,1,1,1]) == 6
assert Solution().numIdenticalPairs([1,2,3]) == 0
print("1512 passed ✅")