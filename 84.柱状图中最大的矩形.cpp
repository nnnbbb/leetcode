/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start

#include <iostream>
#include <stack>
#include <vector>

// using namespace std;
using std::max;
using std::stack;
using std::vector;

// @lc code=start
class Solution {
   public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n, n);

        stack<int> mono_stack;
        for (int i = 0; i < n; ++i) {
            while (!mono_stack.empty() && heights[mono_stack.top()] >= heights[i]) {
                right[mono_stack.top()] = i;
                mono_stack.pop();
            }
            left[i] = (mono_stack.empty() ? -1 : mono_stack.top());
            mono_stack.push(i);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, (right[i] - left[i] - 1) * heights[i]);
        }
        return ans;
    }
};

int main() {
    Solution* s = new Solution();
    vector<int> heights = {6, 7, 5, 2, 4, 5, 9, 3};

    int res = s->largestRectangleArea(heights);
    // printf("res = %d\n", res);
    std::cout << res << ' ';

    return 0;
}
// @lc code=end

