t=int(input())
for i in range(t):
    arr =input()
    lists=arr.split()
    tr=int(lists[0])
    tm=int(lists[1])
    if int(lists[2])%2!=0:
            tr*=2
    if tr>tm:
        print(tr//tm)
    else:    
        print(tm//tr)
 
