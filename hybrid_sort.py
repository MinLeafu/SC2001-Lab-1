import random

def insertion_sort(arr, left, right):
    comparisons = 0

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

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


def hybrid_merge_sort(arr, temp, left, right, S):
    if left >= right:
        return 0

    size = right - left + 1

    if size <= S:
        return insertion_sort(arr, left, right)

    mid = (left + right) // 2
    comparisons = 0

    comparisons += hybrid_merge_sort(arr, temp, left, mid, S)
    comparisons += hybrid_merge_sort(arr, temp, mid + 1, right, S)
    comparisons += merge(arr, temp, left, mid, right)

    return comparisons


def hybrid_sort(arr, S):
    if S < 1:
        raise ValueError("S must be at least 1")

    temp = [0] * len(arr)

    comparisons = hybrid_merge_sort(
        arr,
        temp,
        0,
        len(arr) - 1,
        S
    )

    return comparisons


def generate_data(n, x, seed=None):
    random_generator = random.Random(seed)

    return [
        random_generator.randint(1, x)
        for _ in range(n)
    ]


if __name__ == "__main__":
    input_sizes = [
        1_000,
        10_000,
        100_000,
        1_000_000,
        10_000_000
    ]

    x = 10_000_000

    for n in input_sizes:
        data = generate_data(n, x, seed=42 + n)

        print(f"Dataset size: {len(data):,}")
        print(f"First 10 values: {data[:10]}")
        print(f"Minimum value: {min(data):,}")
        print(f"Maximum value: {max(data):,}")
        print()

        del data