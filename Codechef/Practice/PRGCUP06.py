import math
class node:
    def __init__(self,k,w):
        self.value=k
        self.weight=w
        self.next=None
class node1:
    def __init__(self,k):
        self.value=k
        self.next=None
        self.color='white'
        self.dist=999
        self.pred=None
class adjl:
    def __init__(self,n):
        self.b=[None]*n
        for i in range(n):
            self.b[i]=node1(i)
    def insert(self,v1,v2,w):
        temp=self.b[v1]
        while(temp.next!=None):
            temp=temp.next
        temp2=node(v2,w)
        temp.next=temp2
        temp=self.b[v2]
        while(temp.next!=None):
            temp=temp.next
        temp2=node(v1,w)
        temp.next=temp2
def dfs(g,s,l):
    s.color='grey'
    global distance
    global arr
    temp=s.next
    while(temp!=None):
        if g.b[temp.value].color=='white':
            g.b[temp.value].pred=s
            g.b[temp.value].dist=temp.weight
            distance+=temp.weight
            dfs(g,g.b[temp.value],l)            
        temp=temp.next
    if s.pred!=None:
        loc=math.ceil(arr[s.value]/l)
        distance+=(2*loc-1)*(s.dist)
        arr[s.pred.value]+=arr[s.value]
        arr[s.value]=0
        
n,lim=map(int,input().strip().split())
t2=adjl(n)
arr=[int(x) for x in input().split()]
distance=0
for j in range(n-1):
    g1,g2,g3=map(int,input().split())
    t2.insert(g1-1,g2-1,g3)
dfs(t2,t2.b[0],lim)
print(distance)
