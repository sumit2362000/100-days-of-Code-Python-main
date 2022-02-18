import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

# Show first 5 rows of dataframe
df.head()

# Show last couple rows of dataframe
df.tail()

# Number of rows and columns
df.shape

# Access column names directly
df.columns

# check for Nan(Not A NUmber) values in dataframe
df.isna()

