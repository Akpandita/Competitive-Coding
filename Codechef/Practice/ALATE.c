#include<iostream>
#include<bits/stdc++.h>
#define max1 1000000007
using namespace std;
long long int a[100001],sum[100001];
vector <long long int> v[100001];
 
void initialize(int n)
{
    for(int i=1;i<=n;i++)
    {
        for(int j=i;j<=n;j+=i)
        {
            v[j].push_back(i);
        }
    }
}
int main(){
initialize(100001);
int t,n,q;
scanf("%d",&t);
while(t--)
{
    scanf("%d%d",&n,&q);
    for(int i=1;i<=n;i++)
        scanf("%lld",&a[i]);
    long long int summ;
    for(int i=1;i<=n;i++)
    {
        summ=0;
        for(int j=i;j<=n;j+=i)
        {
            summ=(summ%max1+((a[j]%max1)*(a[j]%max1))%max1)%max1;
        }
        sum[i]=summ;
    }
    int op,x;
    long long int y;
    while(q--)
    {
        scanf("%d",&op);
        if(op==1)
        {
            scanf("%d",&x);
            printf("%d\n",sum[x]);
        }
        else{
            scanf("%d%lld",&x,&y);
            for(int i=0;i<v[x].size()&&i<=n;i++)
            {
                sum[v[x][i]]=(sum[v[x][i]]%max1-((a[x]%max1)*(a[x]%max1))%max1+max1)%max1;
                sum[v[x][i]]=(sum[v[x][i]]%max1+((y%max1)*(y%max1))%max1)%max1;
            }
            a[x]=y;
        }
    }
}
return 0;
}