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
    # c(ii): Fix n and change threshold S
    fixed_n = 1_000_000
    x = 10_000_000

    S_values = [
        1,
        2,
        4,
        8,
        16,
        32,
        64,
        128
    ]

    # Generate one original dataset
    original_data = generate_data(fixed_n, x, seed=42)

    print("Part c(ii): Fixed n, changing S")
    print(f"Fixed n = {fixed_n}")
    print("S,comparisons")

    for S in S_values:
        # Use the same original dataset for every S
        data = original_data.copy()

        comparisons = hybrid_sort(data, S)

        print(f"{S},{comparisons}")

        del data
