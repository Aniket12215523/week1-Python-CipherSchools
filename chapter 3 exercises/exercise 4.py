# problem
# ask user to input a number conataining more than on digit
# example - 1257
# calculate 1+2+5+7

num=(input())
sum=0
i=0
while(i<len(num)):
    sum=sum+int(num[1])
    i=i+1
print(sum)
