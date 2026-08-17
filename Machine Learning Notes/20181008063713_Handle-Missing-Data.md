# Handle Missing Data
> Most libraries (including scikit-learn) will give you an error if you try to build a model using data with missing values. 

[Refer to Kaggle: Handling Missing Values](https://www.kaggle.com/dansbecker/handling-missing-values)

## Solution 1: Drop Columns with Missing Values

In many cases, you'll have both a training dataset and a test dataset. You will want to drop the same columns in both DataFrames.

So, it's somewhat usually not the best solution. However, it can be useful when most values in a column are missing.

## Solution 2: Imputation
> Imputation fills in the missing value with some number. Imputation is the standard approach, and it usually works well.


