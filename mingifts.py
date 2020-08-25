emp=int(input("Enter number of Employees:"))
count=0
rank=[]
for i in range (emp):
     
    r=int(input("Enter rank of #%d employee :" %(i+1)))
    # print()
    rank.append(r)
for i in range(emp-1) :
    for j in range(emp-i-1):
        if rank[j]<rank[j+1] : 
            count+=1
        else:
            count-=1
    
print(count+emp)