t=int(input())
for i in range(t):
    arr=int(input())
    n=arr
    rev=0
    while(int(n)!=0):
        rem=n%10
        rev=int((rev*10)+rem)
        n/=10 
    if(rev==arr):
        print('wins')
    else:
        print('losses')
