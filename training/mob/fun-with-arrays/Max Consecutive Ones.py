class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = map(str, nums)
        s_nums = "".join(nums)
        return len(max(s_nums.split("0")))


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1, 0, 0]))
