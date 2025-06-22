def max_increasing_subarray_length(n, arr):
    max_len = 1
    curr_len = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len
n = int(input())
arr = list(map(int, input().split()))
print(max_increasing_subarray_length(n, arr))
