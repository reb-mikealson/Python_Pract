'''Find Armstrong numbers in a given range.'''
num1=int(input("enter the lower number"))
num2=int(input("enter the upper number"))
for i in range(num1,num2):
    string_i=str(i)
    power=len(string_i)
    sum=0
    for j in string_i:
        sum+=int(j)**power
    if (sum==i):
        print(i)