def pure_merge_sort(arr, temp, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    comparisons = 0

    comparisons += pure_merge_sort(arr, temp, left, mid)
    comparisons += pure_merge_sort(arr, temp, mid + 1, right)
    comparisons += merge(arr, temp, left, mid, right)

    return comparisons


def merge(arr, temp, left, mid, right):
    comparisons = 0

    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        comparisons += 1

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for k in range(left, right + 1):
        arr[k] = temp[k]

    return comparisons


def original_merge_sort(arr):
    temp = [0] * len(arr)
    return pure_merge_sort(arr, temp, 0, len(arr) - 1)