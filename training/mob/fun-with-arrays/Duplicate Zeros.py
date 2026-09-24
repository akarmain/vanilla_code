class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans = []
        for i in arr:
            if str(i) == "0":
                ans.append(0)
            ans.append(i)
        return ans[: len(arr)]


if __name__ == "__main__":
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
