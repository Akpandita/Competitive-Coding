t=int(input())
for i in range(t):
	n=int(input())
	s=[int(x) for x in input().split()]
	arr=[0]*4
	for j in range(len(s)):
		arr[s[j]%4]+=1
	sum=0
	if arr[1]>arr[3]:
		sum+=arr[3]
		arr[1]-=arr[3]
		sum+=(arr[1]//4)*3
		sum+=arr[2]//2
		arr[2]=arr[2]%2
		arr[1]=arr[1]%4
		if arr[1]==0 and arr[2]==0:
			print(sum)
		elif arr[1]==2 and arr[2]==1:
			sum+=2
			print(sum)
		else:
			print('-1')
 
	else:
		sum+=arr[1]
		arr[3]-=arr[1]
		sum+=(arr[3]//4)*3
		sum+=arr[2]//2
		arr[2]=arr[2]%2
		arr[3]=arr[3]%4
		if arr[3]==0 and arr[2]==0:
			print(sum)
		elif arr[3]==2 and arr[2]==1:
			sum+=2
			print(sum)
		else:
			print('-1')
