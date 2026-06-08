import pandas as pd

# 1. Create a Pandas DataFrame with a two-dimensional Python list
data_2d = [
    [1, "Akshita", 19],
    [2, "Aashvi", 20],
    [3, "Akshat", 21]
]
df1 = pd.DataFrame(data_2d, columns=["ID", "Name", "Age"])
print("\nDataFrame from 2D List:")
print(df1)

# 2. Create DataFrame from Python Dictionary
data_dict = {
    "ID": [1, 2, 3],
    "Name": ["Akshita", "Aashvi", "Akshat"],
    "Age": [19, 20, 21]
}
df2 = pd.DataFrame(data_dict)
print("\nDataFrame from Dictionary:")
print(df2)

# 3. Create Pandas DataFrame using List of Lists
list_of_lists = [
    ["Akshita", 19],
    ["Aashvi", 20],
    ["Akshat", 21]
]
df3 = pd.DataFrame(list_of_lists, columns=["Name", "Age"])
print("\nDataFrame from List of Lists:")
print(df3)

# 4. Create Pandas DataFrame using List of Tuples
list_of_tuples = [
    ("Akshita", 19),
    ("Aashvi", 20),
    ("Akshat", 21)
]
df4 = pd.DataFrame(list_of_tuples, columns=["Name", "Age"])
print("\nDataFrame from List of Tuples:")
print(df4)

# 5. Create a Pandas DataFrame from List of Dictionaries
list_of_dicts = [
    {"Name": "Akshita", "Age": 19},
    {"Name": "Aashvi", "Age": 20},
    {"Name": "Akshat", "Age": 21}
]
df5 = pd.DataFrame(list_of_dicts)
print("\nDataFrame from List of Dictionaries:")
print(df5)

# ----------------------------------------------------

df = df2.copy()

# 6. Different ways to iterate over rows in Pandas DataFrame
print("\nUsing iterrows():")
for index, row in df.iterrows():
    print(index, row["Name"], row["Age"])

print("\nUsing itertuples():")
for row in df.itertuples():
    print(row.Name, row.Age)

# 7. Selecting rows in Pandas DataFrame based on conditions
print("\nRows where Age > 19:")
print(df[df["Age"] > 19])

# 8. Select any row from a DataFrame using iloc[]
print("\nFirst Row using iloc:")
print(df.iloc[0])

# 9. Limited rows selection with given column
print("\nFirst 2 rows of Name column:")
print(df.loc[0:1, ["Name"]])

# 10. Drop rows from DataFrame based on condition applied on a column
print("\nAfter dropping rows where Age > 20:")
df_drop = df[df["Age"] <= 20]
print(df_drop)

# 11. Insert row at given position in Pandas DataFrame
new_row = pd.DataFrame({
    "ID": [4],
    "Name": ["Tailor"],
    "Age": [22]
})

df_insert = pd.concat([df.iloc[:1], new_row, df.iloc[1:]]).reset_index(drop=True)

print("\nAfter inserting row at position 1:")
print(df_insert)

# 12. Create a list from rows in Pandas DataFrame
row_list = df.values.tolist()

print("\nList created from DataFrame rows:")
print(row_list)

# 13. Create a list from a specific column
name_list = df["Name"].tolist()

print("\nList of Names:")
print(name_list)
