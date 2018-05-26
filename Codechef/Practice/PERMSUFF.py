t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[int(x) for x in input().split()]
    arr3=[]
    for j in range(n):
        arr3.append(j)
    for j in range(m):
        x,y=map(int,input().split())
        if x<y:
            if arr3[x-1]<y-1:
                arr3[x-1]=y-1
        elif y>x:
            if arr3[y-1]<x-1:
               arr3[y-1]=x-1
    j=0
    while(j<n):
        x=j
        if x==arr3[x]:
            j+=1
        else:
            max1=arr3[x]
            flag=0
            while(1):
                if flag==0:
                    flag=1
                    for k in range(x+1,arr3[x]+1):
                        if max1<arr3[k]:
                            max1=arr3[k]
                    if max1==arr3[x]:
                        break
                    else:
                        prevmax=arr3[x]
                else:
                    y=max1
                    for k in range(prevmax,y+1):
                        if max1<arr3[k]:
                            max1=arr3[k]
                    if prevmax==max1:
                        break
                    else:
                        prevmax=y
            for k in range(x,max1+1):
                arr3[k]=max1
            j=max1+1
    count=0
    for j in range(n):
        if arr[j]-1==j:
            count+=1
        else:
            if j<arr[j]-1:
                if arr3[j]>=arr[j]-1:
                    count+=1
            else:
                if arr3[arr[j]-1]>=j:
                    count+=1
    if count==n:
        print('Possible')
    else:
        print('Impossible')
