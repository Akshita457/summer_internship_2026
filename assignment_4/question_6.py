#6. Write a Python function to check whether a number falls within a given range.
def range():
    num=int(input("Enter number="))
    lower_bound=int(input("Enter lower bound="))
    upper_bound=int(input("Enter upper bound="))
    if (num>=lower_bound or num<=upper_bound):
        print("Number falls in given range")
    else:
        print("Number does not fall within given range")    

range()