n=int (input ("ENTER THE NUMBER\n") )
temp=n
rev=0
while(n>0):
     dig=n%10
     rev=rev*10+dig
     n=n//10

if (temp==rev) :
        print ("GIVEN NUMBER IS PALINDROME")
else:
      print ("GIVEN NUMBER IS NOT PALINDROME")