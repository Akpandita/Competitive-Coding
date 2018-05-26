class node:
    def __init__(self,key):
        self.data=key
        self.parent=None
        self.rank=0
        self.color=None
class disjoint:
    def __init__(self,n):
        self.mapp=[None]*n
        for i in range(n):
            self.mapp[i]=node(i)
            self.mapp[i].parent=self.mapp[i]
    def find(self,a):
        node1=self.mapp[a]
        while(1):
            if node1.parent==node1:
                break
            else:
                node1=node1.parent
        if node1.rank>=2:
            self.mapp[a].parent=node1
        return(node1)
    def union(self,a,b):
        rep1=self.find(a)
        rep2=self.find(b)
        if (rep1.color==0 and rep2.color==1) or (rep2.color==0 and rep1.color==1) :
            return False
        elif rep1.rank==rep2.rank:
            rep1.rank+=1
            rep2.rank=0
            rep2.parent=rep1
        elif rep1.rank>rep2.rank:
            rep1.rank+=1
            rep2.rank=0
            rep2.parent=rep1
        else:
            rep2.rank+=1
            rep1.rank=0
            rep1.parent=rep2
        return True
    def colored(self,a,b):
        rep1=self.find(a)
        rep2=self.find(b)
        if rep1==rep2:
            return False
        elif rep1.color==None and rep2.color==None:
            rep1.color=0
            rep2.color=1
        elif rep2.color==None:
            rep2.color=(rep1.color+1)%2
        elif rep1.color==None:
            rep1.color=(rep2.color+1)%2
        elif rep1.color==rep2.color:
            return False
        return True
t=int(input())
for i in range(t):
    n,q=map(int,input().strip().split())
    d=disjoint(n)
    flag=0
    for j in range(q):
        s0,s1,s2=map(int,input().strip().split())
        if flag==0:
            if s0==s1:
                if s2==1:
                    flag=1
            else:
                if s2==1:
                    if(d.colored(s0-1,s1-1)==False):
                        flag=1
                elif s2==0:
                    if (d.union(s0-1,s1-1)==False):
                        flag=1
    if flag==0:
        print("yes")
    else:
        print("no")
