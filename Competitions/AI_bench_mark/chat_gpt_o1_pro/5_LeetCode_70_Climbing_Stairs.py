class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1

        previous, current = 1, 1

        for i in range(2, n + 1):
            next_step = previous + current
            previous, current = current, next_step

        return current