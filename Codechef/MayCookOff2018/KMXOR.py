import random
t=int(input())
for m in range(t):
    n,k=map(int,input().split())
    #n=random.randint(1,21)
    #k=random.randint(1,21)
    #print(n,k)
    t = str(bin(k))[2:]
    t = t.replace('0','2')
    t = t.replace('1','0')
    t = t.replace('2','1')
    x=int(t,2)
    if x!=0:
        if n%2==0:
            for i in range(n):
                if i==0:
                    print(k,end='')
                    print(" ",end='')
                elif i==1:
                    print(x,end='')
                    print(" ",end='')
                else:
                    print(1,end='')
                    print(" ",end='')
        else:
            if x==1:
                y=x^2
                for i in range(n):
                    if i==0:
                        print(k,end='')
                        print(" ",end='')
                    elif i==1:
                        if y<=k:
                            print(2,end='')
                            print(" ",end='')
                        else:
                            print(1,end='')
                            print(" ",end='')
                    elif i==2:
                        if y<=k:
                            print(y,end='')
                            print(" ",end='')
                        else:
                           print(1,end='')
                        print(" ",end='') 
                    else:
                        print(1,end='')
                        print(" ",end='')
            else:
                y=x^1
                for i in range(n):
                    if i==0:
                        print(k,end='')
                        print(" ",end='')
                    elif i==1:
                        print(y,end='')
                        print(" ",end='')
                    else:
                        print(1,end='')
                        print(" ",end='')
    else:
        if n%2!=0:
            for i in range(n):
                if i==0:
                    print(k,end='')
                    print(" ",end='')
                else:
                    print(1,end='')
                    print(" ",end='')
        else:
            if k-1==0:
                for i in range(n):
                    print(1,end='')
                    print(" ",end='')
            else:
                t = str(bin(k-1))[2:]
                t = t.replace('0','2')
                t = t.replace('1','0')
                t = t.replace('2','1')
                x=int(t,2)
                for i in range(n):
                    if i==0:
                        print(k-1,end='')
                        print(" ",end='')
                    elif i==1:
                        print(x,end='')
                        print(" ",end='')
                    else:
                        print(1,end='')
                        print(" ",end='')
    print()
