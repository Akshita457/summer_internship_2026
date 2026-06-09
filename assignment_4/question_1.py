#1. Write a Python function to find the maximum of three numbers.
def max():
    num1=int(input("Enter 1st number="))
    num2=int(input("Enter 2nd number="))
    num3=int(input("Enter 3rd number="))
    if(num1>num2 and num1>num3):
        print(num1,"is the maximum of the three numbers")
    elif(num2>num1 and num2>num3):
        print(num2,"is the maximum of the three numbers")
    else:
        print(num3,"is the maximum of the three numbers")

max()