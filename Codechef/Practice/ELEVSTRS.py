t=int(input())
for i in range(t):
    arr=input()
    l=arr.split()
    ts=float(l[0])*(2**0.5)/float(l[1])
    te=float(l[0])*2/float(l[2])
    if ts > te:
        print("Elevator")
    else:
        print("Stairs")
