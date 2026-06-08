# Practise Pandas Series

# 	Create a Pandas Series from Dictionary 
import pandas as pd
dict={1:"Mango",2:"Apple",3:"Banana",4:"Cherry"}
series1=pd.Series(dict)
print(series1)

#	Create a Pandas Series from Lists 
lst=[10,20,30,40]
series2=pd.Series(lst)
print(series2)

#	Access the elements of a Series in Pandas  
print(series2[2])
