# Numpy Basic Operations [DRAFT]

```py
import numpy as np
```

## Load Data into Numpy Array / Matrix

Load from a list:
```py
>>> np.array([1,2,3,4])
array([1,2,3,4])
```

Load from Pandas DataFrame:
```py
>>> df
...
>>> np.array(df)

Load from DataFrame.read_csv:
```py
# 1D
>>> np.array(pd.read_csv('xx.csv', headers=None, index=None, names=['v'])['v'])

# 2D
>>> 
```

Load directly from file:
```py

```


## Array / Matrix Operation

> The Numpy Array is just a List with many more convenient methods to operate with.

**Add rows to a 2D matrix:**
```py

```

**Add columns to a 2D matrix:**
```py

```

**Concatenate multiple arrays to an "one-line" array (1D):**
```py
>>> collection = [np.ones(3), np.zeros(5), np.random.randint(1, 10, 10)]
>>> np.concatenate(collection)
array([1., 1., 1., 0., 0., 0., 0., 0., 8., 4., 9., 6., 1., 8., 6., 2., 8., 8.])
```

**Array truncation (Set upper/lower limits to each element):**
```py
>>> D1 = np.random.randint(1,100, 10)
array([59, 86, 61, 24, 73, 56, 25, 19, 54, 61])
>>> low, high = 30, 60
>>> np.clip(D1, low, high)
array([59, 60, 60, 30, 60, 56, 30, 30, 54, 60])
>>> np.clip(15, low, high), np.clip(99, low, high)
30, 60
```


**Sort an array / matrix:**
```py
# 1D array
>>> D1 = np.random.randint(1, 10, size=10)
array([3, 2, 2, 8, 5, 1, 5, 7, 8, 7])

>>> np.sort(D1)
array([1, 2, 2, 3, 5, 5, 7, 7, 8, 8])

# 2D matrix
>>> D2 = np.random.randint(1, 10, size=(3, 5))
array([[9, 3, 3, 3, 5],
       [6, 9, 8, 7, 3],
       [4, 8, 8, 5, 9]])

>>> np.sort(D2)  # sorting of axis=1 by default
array([[3, 3, 3, 5, 9],
       [3, 6, 7, 8, 9],
       [4, 5, 8, 8, 9]])

>>> np.sort(D2, axis=1)
array([[3, 3, 3, 5, 9],
       [3, 6, 7, 8, 9],
       [4, 5, 8, 8, 9]])

>>> np.sort(D2, axis=0)  # Sorting on all directions
array([[4, 3, 3, 3, 3],
       [6, 8, 8, 5, 5],
       [9, 9, 8, 7, 9]])
```


**Scale a matrix by a vector:**
```sh
>>> M = np.random.randint(0, 2, (5, 10))
array([[1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
       [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
       [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]])
>>> vector = np.random.random(10)
array([0.6225718 , 0.09463136, 0.39098449, 0.34272358, 0.41703184,
       0.89421665, 0.67289369, 0.64413252, 0.81518109, 0.65407163])

# Multiple a matrix by a vector (scaler)
>>> M * vector
array([[0.6225718 , 0.09463136, 0.        , 0.        , 0.41703184,
        0.        , 0.        , 0.64413252, 0.        , 0.        ],
       [0.6225718 , 0.09463136, 0.        , 0.34272358, 0.41703184,
        0.        , 0.        , 0.        , 0.        , 0.65407163],
       [0.        , 0.09463136, 0.39098449, 0.        , 0.41703184,
        0.        , 0.67289369, 0.64413252, 0.        , 0.        ],
       [0.        , 0.        , 0.39098449, 0.        , 0.        ,
        0.        , 0.67289369, 0.64413252, 0.        , 0.        ],
       [0.6225718 , 0.09463136, 0.        , 0.        , 0.41703184,
        0.        , 0.67289369, 0.        , 0.        , 0.        ]])

# Divide a matrix by a vector
>>> M / vector
array([[ 1.60624043, 10.56732139,  0.        ,  0.        ,  2.39789844,
         0.        ,  0.        ,  1.55247557,  0.        ,  0.        ],
       [ 1.60624043, 10.56732139,  0.        ,  2.91780334,  2.39789844,
         0.        ,  0.        ,  0.        ,  0.        ,  1.52888452],
       [ 0.        , 10.56732139,  2.55764618,  0.        ,  2.39789844,
         0.        ,  1.48611885,  1.55247557,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  2.55764618,  0.        ,  0.        ,
         0.        ,  1.48611885,  1.55247557,  0.        ,  0.        ],
       [ 1.60624043, 10.56732139,  0.        ,  0.        ,  2.39789844,
         0.        ,  1.48611885,  0.        ,  0.        ,  0.        ]])
```
Refer to: https://stackoverflow.com/questions/19602187/numpy-divide-each-row-by-a-vector-element


## Matrix / Array Generation in any Dimension

Fixed value generation:
```py
# 0s for every value
>>> np.zeros(10)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
>>> np.zeros((3,5))  # size=3*5
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

# 1s for every value
>>> np.ones(10)
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> np.ones((3,5))  # size=3*5
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

# Any fixed value
>>> np.full(10, 7)  # size=10, value=7
array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
>>> np.full((3,5), 7)  # size=3*5, value=7
array([[7, 7, 7, 7, 7],
       [7, 7, 7, 7, 7],
       [7, 7, 7, 7, 7]])
```


### Random Value Generation

Random values:
```py
# Random Integers in a range with specified dimension size
>>> np.random.randint(1, 10, size=10)  # low=1, high=10
array([4, 4, 9, 1, 6, 8, 5, 7, 8, 8])
>>> np.random.randint(1, 10, size=(3,5))
array([[8, 8, 8, 7, 5],
       [6, 9, 1, 4, 6],
       [9, 7, 8, 5, 5]])

# Random decimals (0< x < 1)
>>> M = np.array([1,2,3,4,5])
>>> M
array([1, 2, 3, 4, 5])
>>> np.random.shuffle(M)
>>> M  # <- Notice: this will MODIFY the given array
array([4, 3, 2, 1, 5])
```


## Matrix Computation


### Matrix Multiplication


### Check if a matrix is Symmetric

Refer to: https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy

Simply compare the matrix with its transpose with "allclose":
```py
>>> numpy.allclose(M, M.T)
True
```


## Linear Algebra Computation

```py
# Inverse a matrix (if it's a invertible matrix)
>>> np.linalg.inv(X)

# Pseudo-inverse a matrix (useful when the matrix is non-invertible)
>>> np.linalg.pinv(X)

# Normal Equation
>>> np.linalg.pinv(X.T.dot(X)).dot(X.T.dot(Y))
```
