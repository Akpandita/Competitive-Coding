t=int(input())
for i in range(t):
    arr=input()
    lists=arr.split()
    t=int(lists[0])
    while t>=int(lists[1]):
        t-=int(lists[1])
    print(t) 
