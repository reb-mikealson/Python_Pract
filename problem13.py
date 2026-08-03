n=int(input("enter the size of the array:"))
lst=[]
for i in range(n):
    lst.append(int(input("enter the element:")))
#array input done 
#[7,1,3,4,5,6]
buy=lst[0]
profit=0
for i in range(n):
    buy=min(buy,lst[i])
    profit=max(profit,lst[i]-buy)
print(profit)