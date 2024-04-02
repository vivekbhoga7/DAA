def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def find_k_largest(nums, k):
    bubble_sort(nums)
    
    return nums[:k]

array = [3, 10, 4, 7, 9, 8, 5]
k = 3
print("The", k, "largest elements are:", find_k_largest(array, k))
