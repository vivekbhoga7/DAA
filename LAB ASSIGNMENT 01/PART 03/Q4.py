a = []
n = int(input("Enter the size of the array : "))
print("Enter the elements (only binary) inside the list : ")
for l in range(0,n):
    k = int(input())
    a.append(k)

print(f"a = {a}")

zeros = []
ones = []

for i in range(0,len(a)):
    if (a[i] == 0):
        zeros.append(a[i])
    else:
        ones.append(a[i])

final_output = zeros + ones
print(f"final output =  {final_output}")

