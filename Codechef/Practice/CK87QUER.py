def evaluate(n):
    m=(n)**(1/2.0)-1
    m=int(m)
    sum=4*(m**3)+9*(m**2)+5*m
    sum/=6
    return(sum)
t=int(input())
for i in range(t):
    d=int(input())
    if d<=1:
        print('0')
    elif d<=700:
        d=d-1
        if d==1:
            print('1')
            continue
        x=int(evaluate(d))
        y=int(d**(1/2.0))
        l=y*y
        o=d-l+1
        x+=o*y
        print(x)
    else:
        x=int(evaluate(d-1))
        y=int((d-1)**(1/2.0))
        l=y*y
        o=d-1-l+1
        x+=o*y
        x2=int(evaluate(d-701))
        y2=int((d-701)**(1/2.0))
        l2=y2*y2
        o2=d-701-l2+1
        x2+=o2*y2
        print(x-x2)  
