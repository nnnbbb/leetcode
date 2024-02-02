/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
   public:
    vector<string> res;  // 记录答案
    vector<string> generateParenthesis(int n) {
        dfs(n, 0, 0, "");
        return res;
    }
    void dfs(int n, int lc, int rc, string str) {
        if (lc == n && rc == n) {
            res.push_back(str);  // 递归边界
        } else {
            if (lc < n) {
                dfs(n, lc + 1, rc, str + "(");
            }
            if (rc < n && lc > rc) {
                dfs(n, lc, rc + 1, str + ")");
            }
        };
    }
};

int main() {
    Solution* s = new Solution();
    vector<string> res = s->generateParenthesis(3);
    for (auto const& s : res) {
        std::cout << s << ' ';
    }
    return 0;
}
// @lc code=end
