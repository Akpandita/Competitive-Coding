class stack:
    def __init__(self):
        self.a=[]
        self.top=-1
    def push(self,x):
        self.a.append(x)
        self.top=self.top+1
    def pop(self):
        self.top=self.top-1
        return(self.a[self.top+1])
t=int(input())
for i in range (t):
    k=int(input())
    r=stack()
    s=input()
    flag=0
    for j in range(len(s)):
        if(s[j]=='H'):
            if(r.top==-1):
                r.push(s[j])
            elif r.a[r.top]=='H':
                print('Invalid')
                flag=1
                break
            else:
                r.push(s[j])
        elif(s[j]=='T'):
            if(r.top==-1 or r.a[r.top]=='T'):
                print('Invalid')
                flag=1
                break
            else:
                r.pop()
        else:
            if(s[j]!='.'):
                print('Invalid')
                flag=1
                break
    if(r.top==-1 and flag==0):
        print('Valid')
    elif(r.top!=-1 and flag==0):
        print('Invalid') 
