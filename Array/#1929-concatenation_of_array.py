class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums*2
        return ans
        

# TEST
assert Solution().getConcatenation([1,2,1]) == [1,2,1,1,2,1]
print("1929 passed ✅")