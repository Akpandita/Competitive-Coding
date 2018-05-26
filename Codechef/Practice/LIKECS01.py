t=int(input())
for i in range(t):
    n=input()
    flag=0
    for k in range(len(n)-1):
        for j in range(k+1,len(n)):
            if (n[k]==n[j]):
                flag=1
                break
    if flag==0:
        print('no')
    else:
        print('yes') 
