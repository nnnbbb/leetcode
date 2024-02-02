# 获取某个节点的 parent 公式  parent = (i - 1) / 2
# 获取节点的两个子节点公式    c1     = 2i + 1
# 获取节点的两个子节点公式    c2     = 2i + 2


from typing import List
import unittest
import heapq


# 堆化
def heapify(tree, i):
    n = len(tree)
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max_index = i

    if c1 < n and tree[c1] > tree[max_index]:
        max_index = c1

    if c2 < n and tree[c2] > tree[max_index]:
        max_index = c2

    if max_index != i:
        tree[max_index], tree[i] = tree[i], tree[max_index]
        heapify(tree, max_index)


# 构建一个 heap
def build_heap(tree):
    n = len(tree)
    last_node = n - 1
    # 获取最后一个节点的 parent
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify(tree, i)


# 堆排序
def heap_sort(tree):
    build_heap(tree)
    for i in range(len(tree)-1, -1, -1):
        tree[0], tree[i] = tree[i], tree[0]
        heapify(tree, i)


def heap_push(tree: List[int], item):
    tree.append(item)
    build_heap(tree)


def heap_pop(tree):
    element = tree.pop(0)
    heap_sort(tree)
    return element


class HeapTestCase(unittest.TestCase):
    def test_heapify(self):
        tree = [4, 10, 3, 5, 1, 2]
        heapify(tree, 0)
        self.assertEqual(tree, [10, 5, 3, 4, 1, 2], "test heapify")

    def test_build_heap(self):
        tree = [2, 5, 3, 1, 10, 4]
        build_heap(tree)
        self.assertEqual(tree, [10, 5, 4, 1, 2, 3], "test build heap")
        '''
             10
           /    \
          5      4
         / \    /
        1   2  3
        '''

    def test_heap_sort(self):
        tree = [2, 5, 3, 1, 10, 4]
        heap_sort(tree)
        self.assertEqual(tree, [10, 4, 5, 2, 3, 1], "test heap sort")

    def test_heap_push(self):
        tree = [10, 5, 4, 1, 2, 3]
        heap_push(tree, 11)
        self.assertEqual(tree, [11, 5, 10, 1, 2, 3, 4], "test heap push")

    def test_heap_pop(self):
        tree = [10, 5, 4, 1, 2, 3]
        result = [10, 5, 4, 3, 2, 1]
        for i in range(len(tree)):
            item = heap_pop(tree)
            self.assertEqual(item, result[i], "test heap pop")


if __name__ == '__main__':
    unittest.main()
