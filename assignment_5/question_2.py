#Database Practice
import sqlite3
conn=sqlite3.connect("assignment_db.db")

#create table
conn.execute(
    '''
create table if not exists student(
s_id int primary key,
s_name varchar(20),
s_city varchar(20))'''
)

conn.execute(
    '''
create table if not exists teacher(
t_id int primary key,
t_name varchar(20),
t_city varchar(20))'''
)

conn.execute(
    '''
create table if not exists management(
m_id int primary key,
m_name varchar(20),
m_city varchar(20))'''
)

#insert values
conn.execute("insert into student values('001','Alinesh','Jaipur')")
conn.execute("insert into student values('002','Mridul','Delhi')")

conn.execute("insert into teacher values('101','Nick','Jaipur')")
conn.execute("insert into teacher values('102','James','Mumbai')")

conn.execute("insert into management values('001','Bhupendrea','Jaipur')")
conn.execute("insert into management values('003','Bhumi','Jaipur')")

#Select statement
data=conn.execute("select * from student")
for m in data:
    print(m)

#Updation
conn.execute("update management set m_city='Noida' where m_id='003'")

#Deletion
conn.execute("delete from management where m_id='001'")

#view management after updation and deletion
m_data=conn.execute("select * from management")
for i in m_data:
    print(i)


conn.commit()

conn.close()