class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
        else:
            return [1] + ([0] * len(digits))
        return digits


if __name__ == "__main__":
    ans = Solution()
    print(ans.plusOne([9, 9, 0, 9]))
