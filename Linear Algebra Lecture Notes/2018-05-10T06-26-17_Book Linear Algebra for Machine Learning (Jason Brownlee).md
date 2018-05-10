# Book: Linear Algebra for Machine Learning (Jason Brownlee)

> "Linear algebra is a pillar of machine learning." - Jason

Check [THIS LINK](https://www.scribd.com/document/371769141/Jason-Brownlee-Basics-for-Linear-Algebra-for-Machine-Learning-Discover-the-Mathematical-Language-of-Data-in-Python-2018) for reading book: _Jason-Brownlee-Basics-for-Linear-Algebra-for-Machine-Learning-Discover-the-Mathematical-Language-of-Data-in-Python-2018_

## Linear Algebra Is Important in Machine Learning

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_01.png)

## Study Linear Algebra Too Early

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_02.png)

## Study Too Much Linear Algebra

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_03.png)

## Study Linear Algebra Wrong

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_04.png)

## A Bette Way To Study Linear Algebra

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_05.png)

## What will be learnt in this book

- Vector norms
- Matrix multiplication
- Matrix properties
- Tensor & its operations
- Matrix factorization: `Eigendecomposition` & `Singular Value Decomposition (SVD)`
- `Principal Component Analysis (PCA)`
- `Linear Least Squares Regression`

## Types of Matrices

1. Square Matrix
2. Symmetric Matrix
3. Triangular Matrix
4. Diagonal Matrix
5. Identity Matrix
6. Orthogonal Matrix

## Matrix Operations

1. Transpose
2. Inverse
3. Trace: Gives the sum of all of the diagonal entries of a matrix
4. Determinant
5. Rank: To estimate of the number of linearly independent rows or columns in a matrix. 

## Sparse Matrix

Matrices that contain mostly zero values are called `sparse`, distinct from matrices where most of the values are non-zero, called `dense`. 

> Very large matrices require a lot of memory, and some very large matrices that we wish to work
with are sparse.
In practice, most large matrices are sparse — almost all entries are zeros.

## Matrix Decompositions

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_06.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_07.png)


Most common types of matrix decomposition:
- LU Decomposition
- QR Decomposition
- Cholesky Decomposition

### LU Decomposition

> The factors L and U are triangular matrices. The factorization that comes from `elimination`.

#### LUP Decomposition

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_08.png)


### QR Decomposition

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_09.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_10.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_11.png)

### Cholesky Decomposition

The Cholesky decomposition is for square symmetric matrices where all values are greater than zero, so-called positive deﬁnite matrices. 
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_12.png)
Where L is the Lower triangular matrix, and Lᵀ is its transpose.
Or
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_13.png)
Where U is the Upper Triangular matrix, and Uᵀ is its tranpose.


## Eigendecomposition

> Eigendecomposition of a matrix is a type of decomposition that involves decomposing a square
matrix into a set of eigenvectors and eigenvalues.
One of the most widely used kinds of matrix decomposition is called eigendecomposition, in which we decompose a matrix into a set of eigenvectors and eigenvalues.

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_14.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_15.png)
> Not all square matrices can be decomposed into eigenvectors and eigenvalues

The parent matrix can be shown to be a product of the eigenvectors and eigenvalues:
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_16.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_17.png)

> Almost all vectors change direction, when they are multiplied by A. 
Certain exceptional vectors x are in the same direction as Ax. 
Those are the “eigenvectors”.

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_18.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_19.png)


## Singular Value Decomposition (SVD)

> The Singular Value Decomposition is a highlight of linear algebra.

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_20.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_21.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_22.png)

> The singular value decomposition (SVD) provides another way to factorize a matrix, into singular vectors and singular values. The SVD allows us to discover some of the same kind of information as the eigendecomposition. However, the SVD is more generally applicable.


## Pseudoinverse

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_23.png)
![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_24.png)


## Dimensionality Reduction

![image](2018-05-10T06-26-17_Book Linear Algebra for Machine Learning (Jason Brownlee)_files/img_25.png)

