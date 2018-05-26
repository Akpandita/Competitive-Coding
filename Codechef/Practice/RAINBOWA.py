t=int(input())
for i in range(t):
    n=int(input())
    arr=input()
    flag=0
    lists=arr.split()
    for j in range((n//2)+1):
        if(j!=n-1):
            if(int(lists[j])-int(lists[j+1])<-1 or int(lists[j])-int(lists[j+1])>1):
                flag=1
                print('no')
                break
        if(int(lists[j])!=int(lists[n-j-1])):
            flag=1
            print('no')
            break
        if (int(lists[j])>7 or int(lists[n//2])!=7):
            flag=1
            print('no')
            break
    if flag==0:
       print('yes')   
