m=1000000007
n,k=input().split()
n,k=int(n),int(k)
s=0
arr=[0]*n
for i in range(n):
    if i<k:
        arr[i]=1
        s+=1
    elif i==k:
        arr[i]=s
    else:
        s=((s%m+arr[i-1]%m)%m-arr[i-k-1]%m)%m
        arr[i]=s
print(arr[n-1])
