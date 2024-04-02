def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][1] > key[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def max_activities(activities):
    insertion_sort(activities)
    
    max_activities_count = 0
    current_end_time = 0
    
    for activity in activities:
        start_time, end_time = activity
        if start_time >= current_end_time:
            max_activities_count += 1
            current_end_time = end_time
    
    return max_activities_count

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print("Maximum number of activities performed by a single person:", max_activities(activities))
