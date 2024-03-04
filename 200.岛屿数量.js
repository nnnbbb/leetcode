/*
 * @lc app=leetcode.cn id=200 lang=javascript
 *
 * [200] 岛屿数量
 */

// @lc code=start
/**
 * @param {character[][]} grid
 * @return {number}
 */
// let numIslands = function (grid) {
//   if (grid[0][0] == '0') { return 0 }

//   let n = grid.length
//   let p = grid.map((v, i) => i)

//   for (let i = 0; i < n; i++) {
//     for (let j = 0; j < grid[i].length; j++) {
//       if (grid[i][j] === '1') {
//         union(p, i, j)
//       }
//     }

//   }
//   let set = new Set()
//   grid.map((v, i) => set.add(parent(p, i)))

//   let res = Array.from(set).length
//   return res
// };

// let union = function (p, i, j) {
//   let p1 = parent(p, i)
//   let p2 = parent(p, j)
//   p[p2] = p1
// }

// let parent = function (p, i) {
//   let root = i
//   while (p[root] != root) {
//     root = p[root]
//   }
//   while (p[i] != i) {
//     x = i
//     i = p[i]
//     p[x] = root
//   }
//   return root
// }


class UnionFind {
  constructor(n) { //构造一个节点数为n的集合
    this.count = n //并查集总数
    this.parent = new Array(n)
    this.size = new Array(n)  // size数组记录着每棵树的重量
    for (let i = 0; i < n; i++) {
      this.parent[i] = i; // 自己是自己的parent
      this.size[i] = 1;	//每个集合上节点的数量
    }
  }

  union(p, q) { //连通结点p和结点q, p和q都是索引
    let rootP = this.find(p);
    let rootQ = this.find(q);
    if (rootP === rootQ) return
    // 元素数量小的接到数量多的下面，这样比较平衡
    if (this.size[rootP] > this.size[rootQ]) {
      this.parent[rootQ] = rootP;
      this.size[rootP] += this.size[rootQ];
    } else {
      this.parent[rootP] = rootQ;
      this.size[rootQ] += this.size[rootP];
    }
    this.count--;
  }

  isConnected(p, q) { //判断p,q是否连通
    return this.find(p) === this.find(q)
  }

  find(x) { //找到x结点的root
    while (this.parent[x] != x) {
      // 进行路径压缩
      this.parent[x] = this.parent[this.parent[x]];
      x = this.parent[x];
    }
    return x;
  }

  getCount() { //返回子集个数
    return this.count;
  }

}

var numIslands = function (grid) {
  let m = grid.length
  if (m === 0) return 0
  let n = grid[0].length
  const dummy = -1
  const dirs = [[1, 0], [0, 1]]//方向数组 向右 向下
  const uf = new UnionFind(m * n)
  for (let x = 0; x < m; x++) {
    for (let y = 0; y < n; y++)
      if (grid[x][y] === '0') {//如果网格是0，则和dummy合并
        uf.union(n * x + y, dummy)
      }
      else if (grid[x][y] === '1') {//如果网格是1，则向右 向下尝试
        for (let d of dirs) {
          let r = x + d[0]
          let c = y + d[1]
          if (r >= m || c >= n) continue //坐标合法性
          if (grid[r][c] === '1') { //当前网格的右边 下面如果是1，则和当前网格合并
            uf.union(n * x + y, n * r + c)
          }
        }
      }
  }
  return uf.getCount()  //返回并查集的个数减一就行
};

var numIslands = function (grid) {
  let g = grid
  let dx = [1, -1, 0, 0]
  let dy = [0, 0, 1, -1]
  let result = 0
  var sink = function (i, j) {
    if (g[i][j] == "0") {
      return
    }
    g[i][j] = '0'

    for (let k = 0; k < dx.length; k++) {
      let x = j + dx[k]
      let y = i + dy[k]
      if (y >= 0 && y < g.length && x >= 0 && x < g[i].length) {
        sink(y, x)
      }
    }
    return 1
  }

  for (let i = 0; i < g.length; i++) {
    for (let j = 0; j < g[i].length; j++) {

      if (g[i][j] === '0') {
        continue
      }
      result += sink(i, j)
    }

  }
  return result
}
// let g1 = [
//   ["1", "0", "1", "1", "0", "1", "1"]]
// let g2 = [
//   ["1", "1", "1", "1", "0"],
//   ["1", "1", "0", "1", "0"],
//   ["1", "1", "0", "0", "0"],
//   ["0", "0", "0", "0", "0"]
// ]
// let r = numIslands(g2)
// console.log('r ->', r)
// @lc code=end

