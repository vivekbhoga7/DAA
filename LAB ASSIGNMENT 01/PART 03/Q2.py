a = []
n = int(input("Enter the size of the array : "))
print("Enter the elements inside the list : ")
for l in range(0,n):
    k = int(input())
    a.append(k)

print(a)
max_prod = 0

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i] * a[j] > max_prod):
            max_prod = a[i] * a[j]

print(f"the maximum product is =  {max_prod}")
