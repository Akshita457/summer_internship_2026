#2)Create two DataFrames, df1 and df2, with a common column (e.g., 'ID'). 

#>Perform an inner merge on this common column and display the resulting DataFrame.
import pandas as pd
df1=pd.DataFrame({
    "Id":[101,102,103,104],
    "Name":["Ayush","Anshul","Abhi","Aman"],
    "City":["Jaipur","Lucknow","Pune","Srinagar"]
},index=[1,2,3,4])
df2=pd.DataFrame({
    "Id":[101,102,105,106],
    "Class":[4,8,5,9],
    "Sectoin":["J","L","D","H"]
},index=[1,2,5,6])
print(df1.merge(df2, on="Id", how="inner"))

#Perform a left join of df1 and df2 on the 'ID' column. 
print(df1.merge(df2,on="Id",how="left"))

#Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.
print(df1.merge(df2,on="Id",how="right"))
print(df1.join(df2,how="right",lsuffix="l",rsuffix="r"))


