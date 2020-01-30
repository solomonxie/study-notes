# Pandas Basic Operations [DRAFT]


## Loading Files

### The "Header/Index Hell"

There're plenty of problems if the CSV only contains values without headers and index:
```py
>>> pd.read_csv('1d.csv', headers=None)
>>> pd.to_csv('1d.csv', headers=None, index=False)
```

It cannot directly convert to Numpy array:
```py

```



## Add Rows or Columns

```py
# ADD A ROW AS HEADER
header = ['COL-' + str(i+1) for i in range(10)]
df = pd.read_csv('matrix.csv', names=header)

# APPEND A ROW OF DATA
new_line = pd.Series(range(len(df.columns)), index=df.columns)
df.append(new_line, ignore_index=True)

# INSERT A COLUM
df['New-Col'] = [f'Value{i}' for i in range(len(df))]  # Insert as the last columns
df.insert(0, 'New-Col', [f'Value{i}' for i in range(len(df))])  # Insert as the first column
```


## Smaller Matrix

Specify columns or rows when reading the file (very fast):
```py
import pandas as pd

# SELECT COLUMNS
df = pd.read_csv('matrix.csv', usecols=range(10))
df = pd.read_csv('matrix.csv', usecols=[1,3,5])
df = pd.read_csv('matrix.csv', usecols=['Name', 'Age', 'Location'])

# SELECT ROWS
df = pd.read_csv('matrix.csv', nrows=100)  # Choose first N rows
df = pd.read_csv('matrix.csv', nrows=100)  # Choose first N rows
df = pd.read_csv('matrix.csv', skiprows=range(3, 100))  # Skip a range of rows
df = pd.read_csv('matrix.csv', skiprows=[2, 4, 6])  # Skip some specific rows

# SELECT BOTH COLUMNS & ROWS
df = pd.read_csv('matrix.csv', usecols=range(10), nrows=100)
```


Select columns or rows from the df:
```py
# SELECT COLUMNS
df['Name']  # Select 1 column
df[ ['Name', 'Age'] ]  # Select multiple columns
df[ df.columns[:3] ]  # Select first 3 columns
df.iloc[:, 3:5]  # Select first 4th~6th columns

# SELECT ROWS
df.iloc[:10]  # Select first 10 rows
df[2:5]  # Select 3rd~6th rows

# SELECT BOTH COLUMNS & ROWS
df.iloc[:10, 3:5]  # Select first 10 rows and 4th~6th columns
```


## Revert a matrix

```py
reverted = df.transpose()
# or
reverted = df.T
```

## Iteration
Refer to: https://thispointer.com/pandas-loop-or-iterate-over-all-or-certain-columns-of-a-dataframe/

```py
# Iterate row by row
for index, row in df.iterrows():
    print(index, row)

for index in reversed(range(len(df))):
    print(index, df.iloc[index])

# Iterate column by column
for col_name, col_data in df.iteritems():
    print(col_name)
    print(col_data)

for col_name in df:
    print(col_name)
    print(df[col_name])

for col_name in reversed(df.columns):
    print(col_name)
    print(df[col_name])
```



## Aggregations


```py
# Sum by row
[sum(df.iloc[i]) for i in range(len(df))]
#or
list(df.sum())

# Sum by column
[sum(df.iloc[:, i]) for i in range(len(df.columns))]
#or
df.sum(axis=0)

# Filter rows by row-sum
df[df.sum(axis=1) > 0]

# Filter columns by column-sum

```
