#3. Write a Python function to multiply all the numbers in a list.
def mul():
    lst=list(map(int,input("Enter numbers:").split()))
    a=1
    for x in lst:
        a*=x
    print(a)

mul()        