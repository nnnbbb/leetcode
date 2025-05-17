# 【[轻松掌握动态规划]4.01背包】 https://www.bilibili.com/video/BV1uW4y1G7Gs 邋遢大哥233
# https://www.hello-algo.com/chapter_dynamic_programming/knapsack_problem  hello 算法

def knapsack_dfs(wgt: list[int], val: list[int], i: int, c: int) -> int:
    """0-1 背包：暴力搜索"""
    # 若已选完所有物品或背包无剩余容量，则返回价值 0
    if i == 0 or c == 0:
        return 0
    # 若超过背包容量，则只能选择不放入背包
    if wgt[i - 1] > c:
        return knapsack_dfs(wgt, val, i - 1, c)
    # 计算不放入和放入物品 i 的最大价值
    no = knapsack_dfs(wgt, val, i - 1, c)
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt[i - 1]) + val[i - 1]
    # 返回两种方案中价值更大的那一个
    return max(no, yes)


def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：动态规划"""
    n = len(wgt) # 物品数量
    # 初始化 dp 表
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[i][c] = dp[i - 1][c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]

"""Driver Code"""
if __name__ == "__main__":
    # 物品重量
    wgt = [10, 20, 30, 40, 50]   
    # 物品价值
    val = [50, 120, 150, 210, 240] 
    # 背包容量
    cap = 50 
    # 物品数量
    n = len(wgt) 

    # 暴力搜索
    res = knapsack_dfs(wgt, val, n, cap)
    print(f"不超过背包容量的最大物品价值为 {res}")
    res = knapsack_dp(wgt, val, cap)
    print(f"不超过背包容量的最大物品价值为 {res}")