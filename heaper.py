def sift_down(array, n, end):
    while True:
        highest = n
        child_x = 2 * n + 1
        child_y = 2 * n + 2
        if child_x < end and array[child_x] > array[highest]:
            highest = child_x
        if child_y < end and array[child_y] > array[highest]:
            highest = child_y
        if highest == n:
            return array
        array[n], array[highest] = array[highest], array[n]  # Exchange nth with last
        n = highest


def heapify(arr):
    mid = len(arr) / 2 - 1
    end = len(arr)
    while mid >= 0:
        arr = sift_down(arr, mid, end)
        mid -= 1


def heap_sort(array):
    heapify(array)
    end = len(array) - 1
    while end > 0:
        array[0], array[end] = array[end], array[0]  # Exchange
        array = sift_down(array, 0, end)
        end -= 1
    return array


def search(array, item, left=0, right=0):
    array = heap_sort(array)
    if len(array) > 0:
        right = len(array)
    while left < right:
        middle = int((left + right) / 2)
        median = array[middle]
        if median < item:
            left = middle + 1
        elif median > item:
            right = middle
        else:
            return middle
    return -1


def isExist(anItem, aList):
    if search(aList, anItem) == -1:
        return False
    else:
        return True
