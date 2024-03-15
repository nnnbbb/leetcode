#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.min_stack[-1]:
            self.min_stack.pop()
        return v

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(-1)
print('minStack ->', minStack.stack)

print(minStack.getMin(), minStack.pop())
print(minStack.getMin(), minStack.pop())
print(minStack.getMin(), minStack.pop())
print(minStack.getMin(), minStack.pop())
# print(minStack.pop(), minStack.getMin())

# @lc code=end
