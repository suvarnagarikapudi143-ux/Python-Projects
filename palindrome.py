n=int(input())
rem=0
t=n
while n!=0:
    rem=rem*10+n%10
    n//=10
if t==rem:
    print("'Palindrome")
else:
    print("Not a Palindrome")