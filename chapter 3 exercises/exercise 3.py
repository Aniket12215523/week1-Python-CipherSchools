# sum of whole numbers
# ask a user for whole number(n)
# print total from 0 to n

sum = 0
i = 0
n = int(input("Enter a whole number: "))
while(i <= n):
    sum += i
    i += 1
print(sum)    
