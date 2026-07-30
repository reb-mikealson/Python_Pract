
def isJumping(num):
    num_str=str(num)
    for i in range(len(num_str)-1):
        if abs(int(num_str[i])-int(num_str[i+1]))!=1:
            return False
    return True

num=int(input("enter a number"))
for i in range(1,num+1):
    if isJumping(i):
        print(i)