import time
import random

def insertion_sort(arr, left, right):
    # Sort arr[left:right + 1] using insertion sort
    # Return number of key comparisons

    comparisons = 0

    # Treat arr[left] as initially sorted
    # Insert each remaining element into correct position
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        # Shift elements larger than key to right
        while j >= left:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        # Insert key into correct position
        arr[j + 1] = key

    return comparisons


def merge(arr, temp, left, mid, right):
    # Merge 2 sorted subarrays:
    # arr[left:mid + 1] and arr[mid + 1:right + 1]
    # Return number of key comparisons

    comparisons = 0

    # i points to left subarray
    # j points to right subarray
    # k points to temp subarray

    i = left
    j = mid + 1
    k = left

    # Compare elements from both halves, copy the smaller one
    while i <= mid and j <= right:
        comparisons += 1

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1

    # Copy any remaining elements from left half
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy any remaining elements from right half
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged result back into original array
    for k in range(left, right + 1):
        arr[k] = temp[k]

    return comparisons


def hybrid_merge_sort(arr, temp, left, right, S):
    # Recursive hybrid merge sort
    # Uses insertion sort when current subarray size <= S

    # Base case: subarray with 0 or 1 element already sorted
    if left >= right:
        return 0

    size = right - left + 1

    # Switch to insertion sort for subarrays with size <= S
    if size <= S:
        return insertion_sort(arr, left, right)

    # Otherwise continue with standard merge sort partitioning
    mid = (left + right) // 2
    comparisons = 0

    comparisons += hybrid_merge_sort(arr, temp, left, mid, S)
    comparisons += hybrid_merge_sort(arr, temp, mid + 1, right, S)
    comparisons += merge(arr, temp, left, mid, right)

    return comparisons


def hybrid_sort(arr, S):
    # Wrapper function for hybrid merge sort
    # Allocate temp array once
    # Return number of key comparisons

    if S < 1:
        raise ValueError("S must be at least 1")

    # Reuse 1 temp array for all merge operations
    # Reduces allocation overhead
    temp = [0] * len(arr)

    comparisons = hybrid_merge_sort(
        arr,
        temp,
        0,
        len(arr) - 1,
        S
    )

    return comparisons


def pure_merge_sort(arr, temp, left, right):
    # Standard recursive merge sort
    # Return number of key comparisons

    # Base case: subarray with 0 or 1 element already sorted
    if left >= right:
        return 0

    mid = (left + right) // 2
    comparisons = 0

    # Sort both halves recursively then merge
    comparisons += pure_merge_sort(arr, temp, left, mid)
    comparisons += pure_merge_sort(arr, temp, mid + 1, right)
    comparisons += merge(arr, temp, left, mid, right)

    return comparisons


def original_merge_sort(arr):
    # Wrapper function for standard merge sort
    # Basically hybrid merge sort with S equal to 1

    temp = [0] * len(arr)
    return pure_merge_sort(arr, temp, 0, len(arr) - 1)


def generate_data(n, x, seed=None):
    # Generate n random integers from 1 to x
    # Seed can be provided to reproduce same dataset

    random_generator = random.Random(seed)

    return [
        random_generator.randint(1, x)
        for _ in range(n)
    ]


if __name__ == "__main__":
    # c(i): Fix S and change size n
    fixed_S = 10
    x = 10_000_000

    input_sizes = [
        1_000,
        10_000,
        100_000,
        1_000_000,
        10_000_000
    ]

    print("Part c(i): Fixed S, changing n")
    print(f"Fixed S = {fixed_S}")
    print("n,comparisons")

    for n in input_sizes:
        # Use deterministic seed to reproduce dataset
        data = generate_data(n, x, seed=42 + n)

        # Uncomment these lines to inspect datasets
        # print(f"Dataset size: {len(data):,}")
        # print(f"First 10 values: {data[:10]}")
        # print(f"Minimum value: {min(data):,}")
        # print(f"Maximum value: {max(data):,}")
        # print()

        comparisons = hybrid_sort(data, fixed_S)

        print(f"{n},{comparisons}")

        # Release large array before next generation
        del data

    print()

    # c(ii): Fix n and change threshold S
    fixed_n = 1_000_000

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

    # c(iii): Optimal value for S
    for n in input_sizes:
        original_data = generate_data(n, x, seed=42 + n)

        for S in S_values:
            data = original_data.copy()

            start = time.process_time()
            hybrid_sort(data, S)
            end = time.process_time()

            print(f"n={n}, S={S}: {end - start}s")

    # d): Original vs hybrid merge sort
    fixed_n = 10_000_000
    fixed_S = 8
    original_data = generate_data(fixed_n, x, seed=42)

    # Original merge sort
    data = original_data.copy()

    start = time.process_time()
    original_comparisons = original_merge_sort(data)
    original_time = time.process_time() - start

    del data

    # Hybrid merge sort
    data = original_data.copy()

    start = time.process_time()
    hybrid_comparisons = hybrid_sort(data, fixed_S)
    hybrid_time = time.process_time() - start

    del data

    # Display comparison results
    print("Original merge sort:")
    print(f"Comparisons: {original_comparisons}")
    print(f"CPU time: {original_time:.6f}s")

    print()

    print("Hybrid merge sort:")
    print(f"Comparisons: {hybrid_comparisons}")
    print(f"CPU time: {hybrid_time:.6f}s")