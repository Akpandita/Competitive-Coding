t=int(input())
for i in range(t):
    arr=input()
    lists=arr.split()
    if int(lists[2])%4!=0:
        print("no")
        continue
    if(int(lists[0])>2*int(lists[1])):
        min1=int(lists[0])-int(lists[1])
    else:
        min1=int(lists[1])
    if int(lists[2])//4>=min1 and int(lists[2])//4<=(int(lists[1])+int(lists[0])):
        print("yes")
    else:
        print("no") 
