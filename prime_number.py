# To check given number is Prime Number or not

flag = 0
num= int(input("Enter Number : "))
for i in range(2,num):
    if num%i == 0:
        flag = 1
        break
if flag == 1:
    print("Not Prime")
else:
    print("Prime Number")
