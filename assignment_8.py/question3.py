#3) Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge the resulting DataFrame with the third DataFrame on a common key. T Understand join() vs. merge()
import pandas as pd
df1=pd.DataFrame({
    "ID":[101,102,103],
    "Name":["Siya","Mohit","Ridhi"],
    "Grade":["A","B","B"]
})
df2=pd.DataFrame({
    "ID":[101,102,104],
    "Name":["Siya","Mohit","Deep"],
    "Grade":["A","B","D"]
})
df3=pd.DataFrame({
    "ID":[105,102,103],
    "Name":["Anushka","Mohit","Ridhi"],
    "Grade":["A","B","B"]
})
result=pd.concat([df1,df2],axis=0)
print(result)

print(df1.merge(result,on="ID"))