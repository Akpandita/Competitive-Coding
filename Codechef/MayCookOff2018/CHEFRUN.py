t=int(input())
for m in range(t):
    x1,x2,x3,v1,v2=input().split()
    time1=(int(x3)-int(x1))/int(v1)
    time2=(int(x2)-int(x3))/int(v2)
    if time1==time2:
        print('Draw')
    elif time1>time2:
        print('Kefa')
    else:
        print('Chef')
