# Pandas: How to read specific columns of csv file?

CSV: https://www.pythonprogramming.in/how-to-read-specific-columns-of-csv-file-using-pandas.html
```py
import pandas as pd
df = pd.read_csv("test.csv", usecols=['Wheat','Oil'])
print(df)
```

JSON:
```py
import pandas as pd
df = pd.read_csv("test.json", columns= ['Wheat','Oil'])
print(df)
```
