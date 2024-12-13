#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int tests;
    std::cin >> tests;

    for (int i = 0; i < tests; ++i) {
        int n, H;
        std::cin >> n >> H;

        std::vector<int> damage(n);
        for (int j = 0; j < n; ++j) {
            std::cin >> damage[j];
        }

        std::sort(damage.begin(), damage.end());
        int x = damage[n - 1];
        int y = damage[n - 2];
        int t = H % (x + y);
        int m = H / (x + y);
        int ans;

        if (t == 0) {
            ans = 2 * m;
        } else if (t <= x) {
            ans = 2 * m + 1;
        } else {
            ans = 2 * m + 2;
        }

        std::cout << ans << std::endl;
    }

    return 0;
}
