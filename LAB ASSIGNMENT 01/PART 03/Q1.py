a = []
n = int(input("Enter the size of the array : "))
print("Enter the elements inside the list : ")
for l in range(0,n):
    k = int(input())
    a.append(k)

print(a)
target = int(input("Enter a target element = "))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i] + a[j] == target):
            print((a[i],a[j]))