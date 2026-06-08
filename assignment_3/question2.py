#2) Write a function for basic math operations like add, multiply, substract, divide and use this in your program, take 2 number in2put from user.

def calculator():
    i=(int(input("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter input:")))

    num1=(int(input("Enter 1st number:")))
    num2=(int(input("Enter 2nd number:")))
    if (i==1):
        print("Sum=",num1+num2)
    elif(i==2):
        print("Difference=",num1-num2)
    elif(i==3):
        print("Product=",num1*num2)
    elif(i==4):
        print("Quotient=",num1/num2)
    else:
        print("Invalid input.")            

calculator()
          

    


    
