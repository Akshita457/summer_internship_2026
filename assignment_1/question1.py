#1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

name=input("Enter name of student:")
std_class=input("Enter class:")
eng_marks=int(input("Enter English marks:"))
maths_marks=int(input("Enter Maths marks:"))
cpp_marks=int(input("Enter cpp marks:"))
dbms_marks=int(input("Enter DBMS marks:"))
java_marks=int(input("Enter Java marks:"))

percentage=(eng_marks+maths_marks+cpp_marks+dbms_marks+java_marks)*0.2

print(f"\nName of student={name}\nClass={std_class}\nPercentage={percentage}%")

#4) Find grade using percentage

if (percentage>=60):
    print("\nGrade=A")

elif(percentage>=50 and percentage<60):
    print("\nGrade=B")

elif(percentage>=40 and percentage<50):
    print("\nGrade=C")

elif(percentage>=33 and percentage<40):
    print("\nGrade=D")

else:
    print("\nFail")          