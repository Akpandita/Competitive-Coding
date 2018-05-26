t=int(input())
for i in range(t):
    total=int(input().strip())
    n1=0
    n2=0
    if total!=0:
        ini=input().strip()
        total-=1
        n1+=1
        fin2=""
        for j in range(total):
            fin=input().strip()
            if fin==ini:
                n1+=1
            else:
                if fin2=="":
                    fin2=fin
                n2+=1
        if n1>n2:
            print(ini)
        elif n2>n1:
            print(fin2)
        else:
            print("Draw")
    else:
        print("Draw")
