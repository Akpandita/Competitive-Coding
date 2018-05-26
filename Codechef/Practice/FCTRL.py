t=int(input())
for i in range(t):
    rem=0
    n=int(input())
    while(n!=0):
        rem=rem+(n//5)
        n=n//5
    print(rem)   
