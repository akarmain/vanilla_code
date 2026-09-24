def count_div(n):
    ans = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                ans += 1
            else:
                ans += 2
    return ans


def get_div(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if i != n / i:
                ans.append(n // i)
    return sum(ans)


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if count_div(n) == 4:
                ans += get_div(n)
        return ans


if __name__ == "__main__":
    print()
    s = Solution()
    print(s.sumFourDivisors([21, 21]))
