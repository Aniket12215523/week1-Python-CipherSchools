# Exercise - WATCH Cartoons
# ask user's name and age
# If user's name starts with ('b' or 'B') and age is above 15 then
# Print 'you may watch Cartoons'
# Else print 'sorry, you can't watch cartoons'

name=str(input("Enter user's name: "))
age=int(input("Enter the age of user: "))
if (name[0] =='b' or name[0] =='B') and age >15:
    print("You may watch Cartoons")
else:
    print("sorry,","you can't watch Cartoons")
