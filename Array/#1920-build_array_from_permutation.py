class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
            i += 1
        return ans

def test_build_array():
    sol = Solution()

    assert sol.buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3]
    assert sol.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
    assert sol.buildArray([0]) == [0]

    print("1920 passed ✅")


test_build_array()