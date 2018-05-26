t=int(input())
for i in range(t):
    n=int(input())
    l=input()
    a=[int(x) for x in l.split()]
    flag=0
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    for j in range(n):
        if a[j]==0:
            count+=1
        elif a[j]==1:
            count1+=1
        elif a[j]==-1:
            count2+=1
        elif a[j]<-1:
            count3+=1
        else:
            count4+=1
    if (n==1):
        print('yes')
    elif n==2:
        if a[0]==1 or a[0]==0 or a[1]==1 or a[1]==0:
            print('yes')
        else:
            print('no')
    elif n==3:
        if count>=2 or count1>=2 or (count1==1 and count2==2) or (count>=1 and count1>=1):
            print('yes')
        else:
            print('no')
    else:
        if count4>=2 or count3>=2 or(count4==1 and count3==1) or (count3>=1 and count2>=1) or (count4>=1 and count2>=1) or (count2>=2 and count1==0):
            print('no')
        else:
            print('yes') 
