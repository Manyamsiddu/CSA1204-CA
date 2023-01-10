p=int(input("Enter no. of processors: "))
ct=[]
for i in range (0,p):
    cpi=float(input("Enter the no. of cycles per instructions: "))
    cr=float(input("Enter the clock rate in GHz: "))
    a=1000*cpi/cr
    ct.append(a)
print("The processor has lowest Execution time: ",min(ct))
