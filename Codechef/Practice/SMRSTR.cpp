#include<bits/stdc++.h>
#include<math.h>
#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,q;
        scanf("%d%d",&n,&q);
        unsigned long long int mul=1,l;
        int x2;
        for(int j=0;j<n;j++)
        {
            scanf("%d",&x2);
            if(mul<=1000000000)
                mul=mul*x2;
        }
        for(int j=0;j<q;j++)
        {
            scanf("%d",&x2);
            l=x2/mul;
            printf("%lld ",l);
        }
        printf("\n");
    }
    return 0;