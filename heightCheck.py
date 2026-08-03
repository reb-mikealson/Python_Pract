n=int(input("Enter the size of the array:"))
heights=[]
for i in range(n):
    heights.append(int(input("Enter the height:")))
defaulters=0
lst=[]
for i in range(n):
    lst.append(heights[i])
heights.sort()
for i in range(n):
    if lst[i]!=heights[i]:
        defaulters+=1
print(defaulters)