# display all the prime numbers within the range


lower = int(input("Enter lower element : "))
upper = int(input("Enter upper element : "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
