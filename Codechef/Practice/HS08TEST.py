arr=input()
lists=arr.split()
if (int(lists[0])%5)==0: 
    if(float(lists[0])+0.50 <= float(lists[1])):
        n=float(lists[1])-0.50-float(lists[0])
        print("%.2f" %n)
    else:
        print("%.2f" % float(lists[1]))
else:
    print("%.2f" % float(lists[1])) 
