n=int(input())
arr=[0]*(n+1)
s=input().split()
s=[int(x) for x in s]
for i in range(n):
    if arr[s[i]]==0:
        arr[s[i]]=1
for i in range(n+1):
    if arr[i]==0:
        print(str(i)+" ",end='')
