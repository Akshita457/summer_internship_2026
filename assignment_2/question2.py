#2) Input 2 strings concatinate them and store in another variable. then perform generally used string methods on it like

str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")
concat=str1+" "+str2
print(concat)

#String Methods

#lower()
print(concat.lower())

#upper()
print(concat.upper())

#title()
print(concat.title())

#swapcase()
print(concat.swapcase())

#capitalize()
print(concat.capitalize())

#center()
print(concat.center(120))

#count()
print(concat.count("a"))

#endswith()
concat.endswith("a")

#find()
print(concat.find("y"))

#isalnum()
print(concat.isalnum())

#isdigit()
print(concat.isdigit())

#isnumeric()
print(concat.isnumeric())

#replace()
print(concat.replace("a","A"))