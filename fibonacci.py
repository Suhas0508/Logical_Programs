# Fibonacci Series
# The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. 
# The first two terms of the Fibonacci sequence are 0 followed by 1.


num = int(input("Enter Number : "))
f = 0
s = 1
rem = 0
total = f+s
print(f"{f}, {s}, ",end="")
for i in range(2,num):
    
    print(f"{total}, ", end="")
    f = s
    s = total
    total = f+s
  
