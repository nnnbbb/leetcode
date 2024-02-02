# 归并排序 MergeSort in Python


def merge_sort(array, start, end):
    if start >= end:
        return
    mid = (start + end) >> 1  # (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)


def merge(array, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
        k += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= end:
        temp.append(array[j])
        j += 1

    for n in range(len(temp)):
        array[start+n] = temp[n]


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")


if __name__ == '__main__':
    array = [6, 5, 12, 9, 1]

    merge_sort(array, 0, len(array)-1)

    print("Sorted array is: ")
    print(array)
