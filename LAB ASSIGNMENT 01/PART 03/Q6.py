def two_sum_brute_force(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == K:
                return True, (arr[i], arr[j])
    return False, None

# Testing the function
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_brute_force(arr, K)
if found:
    print("Yes, there exists a pair that sums up to", K, ":", pair)
else:
    print("No such pair exists.")

def two_sum_sorted(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True, (arr[left], arr[right])
        elif current_sum < K:
            left += 1
        else:
            right -= 1
    return False, None

# Testing the function
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_sorted(arr, K)
if found:
    print("Yes, there exists a pair that sums up to", K, ":", pair)
else:
    print("No such pair exists.")
