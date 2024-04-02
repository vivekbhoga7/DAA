def sorting(m):
    arr = []
    for i in m : 
        arr.extend(m)
    
    for j in range(0,len(m)):
        for k in range(j+1,len(m)):
            if(arr[j] > arr[k]):
                temp = arr[j]
                arr[j] = arr[k]
                arr[k]  = temp
    
    return arr



m = int(input("Enter the total number of lists that you want to keep  :"))
n = int(input("Enter the number of elements tha tyou want inside each array : "))

lists = []

for l in range(m):
    k = [int(input()) for b in range(n)]
    k.sort()
    lists.append(k)


sorted_list = sorting(lists)
print(f"Sorted lists : {sorted_list}")


