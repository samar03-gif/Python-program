# program to find prime number

a=int(input("enter a number:"))
for i in range(2,a):
    if a%i!=0:
        print(a,"is a prime number")
        break
    else:
        print(a,"is not prime number")
        break

