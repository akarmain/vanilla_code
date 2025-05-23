class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0

        for i in range(len(nums)):
            if i > max_reachable:
                # If we can't reach index i, return False
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                # If we can reach or exceed the last index, return True
                return True

        return False
