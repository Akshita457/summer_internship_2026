#7. Write a Python function to Print Even Numbers from a Given List
def even_only():
    lst=list(map(int,input("Enter list elements:").split()))
    for x in lst:
        if x%2==0:
            print(x)
even_only()            

