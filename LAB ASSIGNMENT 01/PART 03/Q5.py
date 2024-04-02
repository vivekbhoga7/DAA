a = []
n = int(input("Enter the size of the array : "))
print("Enter the elements inside the list : ")
for l in range(0,n):
    k = int(input())
    a.append(k)

print(a)
invs = []

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i] > a[j]):
            invs.append( (a[i],a[j]))


print(tuple(invs))
print(f"the total count of inversions is = {len(invs)}")