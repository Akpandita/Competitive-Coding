#include<stdio.h>
int main()
{
 int i,t,j,n,k,a[10][2];
 scanf("%d",&t);
    for(i=0;i<t;i++)
    {   int prod=0,x=0;
        scanf("%d%d",&n,&k);
        for(j=0;j<n;j++)
        {
            scanf("%d%d",&a[j][0],&a[j][1]);
        }
        for(j=0;j<n+1;j++)
        {
 
            if(x>k){
 
                prod+=(x-k)*a[j-1][1];
                x=k;
            }
            if(x==k && j!=n){
                prod+=a[j][0]*a[j][1];
              }
            else if(x!=k && j!=n){
                x+=a[j][0];
            }
        }
    printf("%d\n",prod);
    }
}