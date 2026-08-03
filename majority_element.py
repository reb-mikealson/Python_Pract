n=int(input("Enter the size of the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element:")))
arr.sort()
majority_element=arr[n//2]
print(majority_element)