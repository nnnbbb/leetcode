# 归并排序 MergeSort in Python


def merge_sort(array):
    if len(array) > 1:
        # print('array ->', array)

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Sort the two halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")


if __name__ == '__main__':
    array = [6, 5, 12, 9, 1]

    merge_sort(array)

    print("Sorted array is: ")
    print(array)
