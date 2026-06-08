#1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.
import csv
data=[
    "name","address","mobile","email"
]

with open ("address_book.csv","w",newline='') as file:

    writer=csv.writer(file)
    

    writer.writerow(data)
    num=int(input("Number of entries you want to do:"))
    for i in range(num):
        print("Enter details\n")
        name=input("Enter name:")
        address=input("Enter address:")
        mobile=input("Enter mobile number:")
        email=input("Enter email:")
        writer.writerow([name,address,mobile,email])
print("data inserted in file")        
