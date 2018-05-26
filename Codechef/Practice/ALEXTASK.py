def lcm(a,b):
    x=a
    y=b
    if(a==b):
        return a
    while(1):
        if b>a:
            b=b%a
            if b==0:
                return x*y//a
        else:
            a=a%b
            if a==0:
                return x*y//b
t=int(input())
for i in range(t):
    n=int(input())
    ab = [0]*(n*(n-1)//2)
    arr=input()
    lists=arr.split()
    m=0
    for j in range(n-1):
        for k in range(j+1,n):
            ab[m]=lcm(int(lists[j]),int(lists[k]))
            m=m+1
    min1=ab[0]
    for j in range(1,n*(n-1)//2):
        if(min1>ab[j]):
            min1=ab[j]
    print(min1) 
