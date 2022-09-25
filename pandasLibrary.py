data = {
    "ages": [14, 18, 24, 42],
    "heights": [165, 180, 176, 184]
}

# df = pd.DataFrame(data)

df = pd.DataFrame(data, index=['James', 'Bob', 'Daniela', 'John'])
print(df)

# return only the row if index is equals
print(df.loc["John"])

# return only the columns/series specified
print(df["ages"])

# third row
print(df.iloc[2])

# first 3 rows
print(df.iloc[:3])

# rows 2 to 3
print(df.iloc[1:3])

# final row
print(df.iloc[-1])

# conditions
print(df[(df['ages'] > 18) & (df['heights'] > 180)])

# reading documents with pandas
df = pd.read_csv('https://www.sololearn.com/uploads/ca-covid.csv')
print(df.head())
print(df.head(10))

# get the final rows
print(df.tail(20))

# get info the data in the dataframe
print(df.info())

# generate index for dataFrame
df.set_index('date', inplace=True)

# delete one column
df.drop('state', axis=1, inplace=True)
# drop() delete rows and columns
# axis = 1 we specify the name of column we want to delete
# axis = 0 delete one row

# resume of statistics
df.describe()

# return the frequency of values in dataframe
df['month'].value_counts()

# group data
print(df.groupby('month')['cases'].sum())
