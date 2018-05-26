t=int(input())
for i in range(t):
    n=int(input())
    rev=0
    while(int(n)!=0):
        rem=n%10
        rev=int((rev*10)+rem)
        n/=10
    print(rev)    
