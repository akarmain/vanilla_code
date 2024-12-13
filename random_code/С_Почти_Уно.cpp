#include <iostream>
#include <vector>
#include <string>

int main() {
    std::string s1;
    std::cin >> s1;

    std::vector<std::string> s2(5);
    for (int i = 0; i < 5; ++i) {
        std::cin >> s2[i];
    }

    std::vector<int> ans;
    for (int i = 0; i < 5; ++i) {
        if (s2[i][0] == s1[0] || s2[i][0] == 'b' || s2[i][1] == s1[1]) {
            ans.push_back(i + 1);
        }
    }

    if (ans.empty()) {
        std::cout << "NO" << std::endl;
    } else {
        std::cout << "YES" << std::endl;
        for (int i : ans) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
