x=int(input())
for i in range(x):
    sum1=0
    p=0
    j=0
    t=int(input())
    while j>=0:
        p=(t-2)/2
        sum1+=j
        j, d = divmod(p, 1)
        t-=2
    if sum1<0:
        sum1=0
    print(int(sum1)) 
