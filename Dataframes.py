import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = a
# returns the first few rows (the “head” of the DataFrame). :
df.head()

# shows information on each of the columns, such as the data type and number of missing values. :
df.info()

# returns the number of rows and columns of the DataFrame.: 
df.shape

# calculates a few summary statistics for each column. :
df.describe()

# A two-dimensional NumPy array of values. :
df.values

# An index of columns: the column names. :
df.columns

#An index for the rows: either row numbers or row names.
df.index

# to sort :
df.sort_values(["",""], [asceding=True, False])

#subsettings columns:
df[["",""]]

# To subset rows :
df[df["",""] > 50] 

# To subset based on text data : 
df[df[""]==""]

# Multiple Condition : 
df[(df[""]=="") & (df[""] =="")]

# To check if it's in : 
variable = 2
df[""].isin[variable]

# To add new column
df[""] =df[""] + df[""]

# To summarize numeral data :
df.mean()
df[""].min()

# To apply a function to df :
df[["",""].agg([function,function])]
   
# To drop Duplicates :
a =df.drop_duplicates(subset=["",""])(subset ="")

# To count values :
a["column"].value_counts(sort=True, normalize=True)

# Summaries by group :
df.groupby("")[""].mean()
df.groupby("")[""].agg([min,max,sum])
df.groupby(["",""])[""].mean()
df.groupby(["",""])[["",""]].mean()

#Pivot tables:
df.pivot_table(values="",index="", columns ="", aggfunc=[np.median, np.mean], fill_value=0, margins=True)

#Explicit indexes
df = df.set_index("") -> df = df.set_index(["",""])
df.reset_index(drop=True)
df.loc[""] -> df.loc[["",""]] -> df.loc[[("",""),("","")]]

#Slicing lists
df.set_index(["",""]).sort_index()
df.loc["Chow chow":"Poodle"]
df.loc[("column","column"):("column","column"),"row":"row"]
df =[2:5]

#subsetting by row/column number
df.iloc[2:5,1:4] ("row, column")

#Calculation summary stats across columns
df.mean(axis="columns")

#.loc[] + slicing
df.loc["":""]

#get the months
df["column"].dt.month
df["column"].dt.year

#import matplotlib.pyplot as plt
df[""].hist(bins=0,kind="bar",title="",)
df.plot(x="date",y="weight_kg",kind="line",rot=0)
df[df["sex"]=="F"]["height_cm"].hist(alpha=0.7)
plt.legend(["F","M"])
plt.show()

#Missing values
df.isna().any()
df.isna().sum().plot(kind="bar")
df.dropna()
df.fillna(0)

#Dictionaries in DF
list_of_dicts =[]
pd.DataFrame(list_of_dicts)

#pull data from csv
pd.read_csv("csv file")
df.to_csv("filepath.csv")

#Inner join
otherdf = 1
df.merge(otherdf, on = "column", suffixes=("_ward","_column"), how="left", left_on="", right_on="")



import pandas as pd
import re

columns = [
    "Building condition",
    "Number of frontages",
    "Surroundings type",
    "Living area",
    "Living room surface",
    "Kitchen type",
    "Bedrooms",
    "Bathrooms",
    "Shower rooms",
    "Toilets",
    "Basement",
    "Furnished",
    "Terrace",
    "Elevator",
    "Swimming pool",
    "Energy class",
    "Heating type",
    "Price",
    "Address",
    "Flood zone type",
    "Garden surface",
    "Terrace surface",
    "Garden",
]

old_csv = pd.read_csv("assets/immoweb_properties_data.csv")

good_csv = old_csv[old_csv["url"].str.contains("new-real-estate-project") == False]

new_columns = good_csv[columns]
missing_values = new_columns.isnull().sum()

purified_csv = new_columns.to_csv("assets/new.csv")
missing_values_csv = missing_values.to_csv("assets/missing_values.csv")


test = new_columns.dropna(subset=["Living area", "Bedrooms", "Price"])
abcd = test.fillna({"Furnished": "None", "Elevator": "None", "Swimming pool": "None"})


# removing Terrasse Surface columns by adding it to Terrace
abcd["Terrace"] = abcd["Terrace"].replace("Yes", 1).fillna(0)
abcd["Terrace surface"] = (
    abcd["Terrace surface"].str.extract(r"([0-9]{1,3})").astype(float)
)
abcd["Terrace"] = (
    abcd[["Terrace", "Terrace surface"]].sum(axis=1, skipna=False).fillna(0)
)

# remonving Garden Surface column by adding it to Garden
abcd["Garden"] = abcd["Garden"].replace("Yes", 1).fillna(0)
abcd["Garden surface"] = (
    abcd["Garden surface"].str.extract(r"([0-9]{2,5})").astype(float)
)
abcd["Garden"] = abcd[["Garden", "Garden surface"]].sum(axis=1, skipna=False).fillna(0)
abcd = abcd.drop(columns=["Terrace surface", "Garden surface"])

abcd["Price"] = abcd["Price"].str.extract(r"([0-9]{4,7})").astype(int)

abcd["Living room surface"] = (
    abcd["Living room surface"].str.extract(r"([0-9]{1,5})").astype(float)
)

abcd["Living area"] = abcd["Living area"].str.extract(r"([0-9]{1,5})").astype(int)

abcd = abcd.fillna("None")

abcd = abcd.replace(["Yes", "No"], [1, 0])

abcd.to_csv("assets/test.csv")

# new_columns.loc["Basement":"Monthly charges"]

