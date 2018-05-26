t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    s3=""
    for j in range(len(s1)):
        if s1[j]=='W' and s2[j]=='W':
            s3+='B'
        elif s2[j]=='B' and s1[j]=='B':
            s3+='W'
        else:
            s3+='B'
    print(s3)
