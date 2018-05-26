t=int(input())
for i in range(t):
    count=0
    l=input().split()
    m=input().split()
    n=input().split()
    b=list(set(m) & set(n))
    print(len(b)) 
