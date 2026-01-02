class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findNumbers([1, 11, 1, 10, 11, 1, 1, 0]))
