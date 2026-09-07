def original_merge_sort(arr, start, end):
    if start >= end:
        return

    mid = start + (end - start) // 2
    original_merge_sort(arr, start, mid)
    original_merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    comparisons = 0

    temp = [0] * (end - start + 1)
    idx = 0
    l, r = start, mid + 1

    while l <= mid and r <= end:
        comparisons += 1

        if arr[l] <= arr[r]:
            temp[idx] = arr[l]
            l += 1
        else:
            temp[idx] = arr[r]
            r += 1
        idx += 1

    while l <= mid:
        temp[idx] = arr[l]
        l += 1
        idx += 1

    while r <= end:
        temp[idx] = arr[r]
        r += 1
        idx += 1

    for i in range(start, end + 1):
        arr[i] = temp[i - start]