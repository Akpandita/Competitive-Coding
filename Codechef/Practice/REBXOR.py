import numpy
maximum=1000000
class xortrie:
    def __init__(self):
        self.treeArray=numpy.empty((maximum,2))
        self.treeArray.fill(-1)
        self.idx=0
    def insert(self,x):
        node=0
        for i in range(31,-1,-1):
            node=int(node)
            if x&(1<<i):
                if self.treeArray[node][1]==-1:
                    self.idx+=1
                    self.treeArray[node][1]=self.idx
                    node=self.idx
                else:
                    node=self.treeArray[node][1]
            else:
                if self.treeArray[node][0]==-1:
                    self.idx+=1
                    self.treeArray[node][0]=self.idx
                    node=self.idx
                else:
                    node=self.treeArray[node][0]
    def search(self,x):
        y=0
        node=0
        for i in range(31,-1,-1):
            node=int(node)
            if x&(1<<i):
                if self.treeArray[node][0]!=-1:
                    node=self.treeArray[node][0]
                else:
                    node=self.treeArray[node][1]
                    y=y+(1<<i)
            else:
                if self.treeArray[node][1]!=-1:
                    node=self.treeArray[node][1]
                    y=y+(1<<i)
                else:
                    node=self.treeArray[node][0]
        return y
n=int(input())
arr=[int(x) for x in input().split()]
pre=0
a=[0]*n
b=[0]*n
pre=arr[0]
a[0]=arr[0]
trie1=xortrie()
trie2=xortrie()
trie1.insert(arr[0])
for i in range(1,n):
    pre=pre^arr[i]
    a[i]=trie1.search(pre)
    a[i]=a[i]^pre
    if (pre>a[i]):
        a[i]=pre
    trie1.insert(pre)
pre=arr[n-1]
b[n-1]=arr[n-1]
trie2.insert(arr[n-1])
for i in range(n-2,-1,-1):
    pre=pre^arr[i]
    b[i]=trie2.search(pre)
    b[i]=b[i]^pre
    if (pre>b[i]):
        b[i]=pre
    trie2.insert(pre)
for i in range(n-2,-1,-1):
    if b[i]<b[i+1]:
        b[i]=b[i+1]
max1=arr[0]
for i in range(n-1):
    if a[i]+b[i+1]>max1:
            max1=a[i]+b[i+1]
print(max1)
