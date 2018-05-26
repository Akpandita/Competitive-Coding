#include<stdio.h>
#define MAX 10000000
int tree[MAX][2];
int idx;
void init(){
int i;
for(i=0;i<MAX;i++)
    {
        tree[i][0]=-1;
        tree[i][1]=-1;
    }
idx=0;
}
void insert(int x){
int node=0,i;
    for(i=31;i>=0;i--)
    {
        if(x&(1<<i)){
            if (tree[node][1]==-1){
            idx++;
            tree[node][1]=idx;
            node=idx;
        }
        else{
            node=tree[node][1];
        }
        }
        else{
            if (tree[node][0]==-1){
                idx++;
                tree[node][0]=idx;
                node=idx;
            }
            else{
            node=tree[node][0];
            }
        }
    }
}
int search(int x){
    int y=0,i;
    int node=0;
    for(i=31;i>=0;i--){
        if(x&(1<<i)){
            if(tree[node][0]!=-1){
                node=tree[node][0];
        }else{
            node=tree[node][1];
            y=y+(1<<i);
        }
    }
    else{
        if(tree[node][1]!=-1){
            node=tree[node][1];
            y=y+(1<<i);
        }else{
            node=tree[node][0];
            }
        }
    }
return y;
}
int maxihum(int a,int b)
{
    if(a>b)
        return a;
    return b;
}
int main(){
init();
int n,i;
scanf("%d",&n);
int arr[n];
for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
int pre=arr[0];
insert(arr[0]);
int sum1[n];
sum1[0]=arr[0];
for(i=1;i<n;i++)
{
    pre=pre^arr[i];
    sum1[i]=search(pre);
    sum1[i]=sum1[i]^pre;
    sum1[i]=maxihum(sum1[i],pre);
    insert(pre);
}
init();
pre=arr[n-1];
insert(arr[n-1]);
int sum2[n];
sum2[n-1]=arr[n-1];
for(i=n-2;i>=0;i--){
    pre=pre^arr[i];
    sum2[i]=search(pre);
    sum2[i]=sum2[i]^pre;
    sum2[i]=maxihum(sum2[i],pre);
    insert(pre);
}
for(i=n-2;i>=0;i--)
    if (sum2[i]<sum2[i+1])
        sum2[i]=sum2[i+1];
int great=arr[0];
for(i=0;i<n-1;i++)
    if (sum1[i]+sum2[i+1]>great)
        great=sum1[i]+sum2[i+1];
printf("%d\n",great);
}