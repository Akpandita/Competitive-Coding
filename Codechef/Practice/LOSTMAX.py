tr=0
t=int(input())
for i in range(t):
    arr =input()
    lists=arr.split()
    for j in range(len(lists)):
         if int(lists[j])==(len(lists)-1):
              tr=j
              break
    if tr!=0:
        maxx=int(lists[0])
    else:
        maxx=int(lists[1])
        
    for j in range(len(lists)):
        if maxx<int(lists[j])and j!=tr:
            maxx=int(lists[j])
    print(maxx)  
