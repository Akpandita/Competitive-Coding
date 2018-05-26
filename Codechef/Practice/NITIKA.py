t=int(input())
for i in range(t):
    strn=input()
    n=0
    m=0
    for j in range(len(strn)):
        if(strn[j]==' 'and n==0):
            n=j
            print(strn[0].upper() + ". ",end='')
        elif(strn[j]==' '):
            m=j
            print(strn[n+1].upper() + ". ",end='')
            break
    if n!=0 and m!=0 :
        for j in range(m+1,len(strn)):
            if(j==m+1):
               print(strn[j].upper(),end='')
            else:
                print(strn[j].lower(),end='')
    if(n==0 and m==0):
        for j in range(len(strn)):
            if(j==0):
                print(strn[0].upper(),end='')
            else:
                print(strn[j].lower(),end='')
               
    if (n!=0 and m==0):
        for j in range(n+1,len(strn)):
            if(n!=0 and m==0 and j==n+1):
                print(strn[n+1].upper(),end='')
            else:
                print(strn[j].lower(),end='')
               
    print()   
