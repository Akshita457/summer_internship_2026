#3) Write a program to check Palindrome Number

#method 1
a=input("Enter your input:")
reverse=a[::-1]
if reverse==a:
    print("Input is palindrome")
else:
    print("Input is not palindrome")

#method 2
num=int(input("Enter number:"))
original=num
rev=0
while(num>0):
    x=num%10
    rev=rev*10+x
    num=num//10

if original==rev:
        print("Number is palindrome")
