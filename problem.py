'''Count integers in a given range, defined by two values, start and end (both inclusive), which are divisible by 3 and the sum of its digits is even.'''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
cnt=0
for i in range(num1,num2+1):
    sum=0
    if (i%3==0):
        while(i>0):
            sum+=i%10
            i//=10
        if(sum%2==0):
            cnt+=1
    else:
        continue
print(cnt)


