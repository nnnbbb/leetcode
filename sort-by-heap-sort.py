# @see https://docs.python.org/zh-tw/3/library/heapq.html
from heapq import heappush, heappop


def heap_sort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


if __name__ == '__main__':
    r = heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(r)
