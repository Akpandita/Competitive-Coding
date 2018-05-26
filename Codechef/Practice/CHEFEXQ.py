import math
#m=100000
class decomp:
    def __init__(self,n,arr):
        self.size=math.ceil(n**0.5)
        self.block2=[]
        self.countarr=[]
        bno=1
        for i in range(n):
            if i//self.size!=bno:
                pre=0
                self.block2.append([])
                self.countarr.append({})
            bno=i//self.size
            pre=pre^arr[i]
            self.block2[bno].append(pre)
            try:
                self.countarr[bno][pre]+=1
            except:
                self.countarr[bno][pre]=1
    def update(self,arr,index,value,n):
        bno=index//self.size
        if index%self.size==self.size-1:
            self.countarr[bno][self.block2[bno][index%self.size]]-=1
            self.block2[bno][index%self.size]=self.block2[bno][self.size-2]^arr[self.size*bno+self.size-1]
            try:
                self.countarr[bno][self.block2[bno][index%self.size]]+=1
            except:
                self.countarr[bno][self.block2[bno][index%self.size]]=1
            return
        elif index%self.size==0:
            pre=0
        else:
            pre=self.block2[bno][(index%self.size)-1]
        for i in range(index%self.size,self.size):
            if bno*self.size+i==n:
                break
            self.countarr[bno][self.block2[bno][i]]-=1
            pre=pre^arr[self.size*bno+i]
            self.block2[bno][i]=pre
            try:
                self.countarr[bno][pre]+=1
            except:
                self.countarr[bno][pre]=1
    def query(self,arr,index,k):
        bno=index//self.size
        pre=k
        count=0
        for i in range(bno):
            try:
                count+=self.countarr[i][pre]
                pre=pre^self.block2[i][-1]
            except:
                pre=pre^self.block2[i][-1]
        x=index%self.size+1
        for i in range(x):
            if pre==self.block2[bno][i]:
                count+=1
        return count
N,Q=map(int,input().split())
arr=[int(x) for x in input().split()]
dem=decomp(N,arr)
for i in range(Q):
    op=[int(x) for x in input().split()]
    if op[0]==1:
        arr[op[1]-1]=op[2]
        dem.update(arr,op[1]-1,op[2],N)
    else:
        print(dem.query(arr,op[1]-1,op[2]))
