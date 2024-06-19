#include <cstdio>
#include <iomanip>  // 包含头文件以使用 std::fixed 和 std::setprecision
#include <iostream>
// using std::cout;
// using std::endl;
// using std::fixed;
// using std::scientific;
// using std::setprecision;
using namespace std;  // 引入 std 命名空间

float InvSqrt(float x) {
    float xhalf = 0.5f * x;
    int i = *(int*)&x;
    i = 0x5f3759df - (i >> 1);
    x = *(float*)&i;
    x = x * (1.5f - xhalf * x * x);
    return x;
}
int main() {
    // InvSqrt(value)函数相当于1.0/sqrt(value)
    // https://blog.csdn.net/qq_37963615/article/details/103428951
    float r = InvSqrt(16);
    printf("%.2f\n", r);
    cout << fixed << setprecision(2) << r << endl;
    return 0;
}