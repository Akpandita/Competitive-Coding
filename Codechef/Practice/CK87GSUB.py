import math
t=int(input())
for i in range(t):
    n=input()
    count=0
    if len(n)<=1:
        print(0)
        continue
    else:
        i=0
        j=1
        flag=0
        if n[i]==n[j]:
            count+=1
        i+=1
        j+=1
        while(j<len(n)):
            if n[i-1]==n[j] and n[i]!=n[j]:
                count+=1
                i+=1
                j+=1
            elif n[i]==n[j]:
                count+=1
                if i!=0:
                    if flag==0:
                        k=i-1
                        flag=1
                i+=1
                j+=1
            else:
                if flag==1:
                    if n[k]==n[j]:
                        count+=1
                    flag=0
                i+=1
                j+=1
        j=1
        count1=1
        while(j<len(n)):
            if n[j]==n[j-1]:
                count1+=1
            else:
                if count1>2:
                    x=math.factorial(count1)/(math.factorial(count1-2)*math.factorial(2))
                    count+=int(x)-count1+1
                count1=1
            j+=1
        if count1>2:
            x=math.factorial(count1)/(math.factorial(count1-2)*math.factorial(2))
            count+=int(x)-count1+1
    print(count)
