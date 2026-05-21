#2. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def func():
    new_list=[]
    input_list=[]
    n=int(input("Number of elements:"))
    for i in range(n):
        element=int(input("Enter element:"))
        input_list.append(element)

    for x in input_list:
        if x not in new_list:
            new_list.append(x)
    return(new_list)


print(func())


