def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_intervals(intervals):
    insertion_sort(intervals)
    
    merged_intervals = []
    merged_interval = intervals[0]
    
    for interval in intervals[1:]:
        if interval[0] <= merged_interval[1]:  
            merged_interval = (merged_interval[0], max(merged_interval[1], interval[1]))
        else:  
            merged_intervals.append(merged_interval)
            merged_interval = interval
    
    merged_intervals.append(merged_interval)
    
    return merged_intervals

intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
print("Non-overlapping intervals after merging:", merge_intervals(intervals))
