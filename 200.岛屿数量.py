#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def sink(i, j):
            if grid[i][j] == "0":
                return 0
            grid[i][j] = '0'
            for k in range(len(dx)):
                x = i + dx[k]
                y = j + dy[k]
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]):

                    if grid[x][y] == '0':
                        continue
                    sink(x, y)
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                lands += sink(i, j)
        return lands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        f = {}  # 定义 "节点 -> 父亲" 的字典

        def find(x):
            # 如果在字典中x不存在，则x自身就是父亲，否则跳过
            f.setdefault(x, x)
            # 递归查找父亲，并给每一个节点设置的都是父亲的值，这里有路径压缩
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        # 合并两个节点的父亲，并把x的父亲改为y的父亲，即将x合并到y的父亲上去，此处没有按秩合并
        def union(x, y):
            print('y ->', y)
            f[find(x)] = find(y)

        if not grid:
            return 0  # 为空，结束
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                # 如果grid[i][j]为岛屿
                if grid[i][j] == "1":
                    # 尝试扫描该岛的 左/上边
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        # 判断数组是否溢出，并判断 左/上是否为岛屿
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                            # 符合if条件，两点联合
                            union(tmp_i * row + tmp_j, i * row + j)
        # print(f)　
        res = set()  # 定义结果集合，方便去重
        for i in range(row):  # 再次遍历
            for j in range(col):
                if grid[i][j] == "1":
                    n = i * row + j
                    print('n ->', i, row, j, n)
                    res.add(find(n))  # 添加父节点到集合中，即使会存在重复的父节点。
        return len(res)  # 返回集合里父节点的数量，即岛屿的个数


g1 = [["1", "0", "1", "1", "0", "1", "1"]]
g2 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
c = Solution()
r = c.numIslands(g2)
print('r ->', r)

# @lc code=end
