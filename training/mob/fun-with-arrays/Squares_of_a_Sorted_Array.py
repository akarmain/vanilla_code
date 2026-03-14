class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: int(x**2), nums)))


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
