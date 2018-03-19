# `Polynomial long division`

[Refer to Wiki: `Polynomial long division`](https://en.wikipedia.org/wiki/Polynomial_long_division)

> It's very import to understand it in the first place. Once get the idea, it's easy to solve this problem.

First need to understand, 
this usually is a **`Degrading process`**.

For instance, we don't need to divide `7/13` or `2/3`, 
because the `numerator` is lower than the `dominator`. 
But we could divide `20/7` to `2 6/7`, and the `6/7` is the `remainder`.

In `polynomials division`, we don't compare the value of them, 
but we could compare the `degrees` of both parts. 
`Higher one` CAN BE divided by a `lower one`, 
and probably left over a `remainder` that even lower than the `dominator`.


There're a few main ideas act in the division process:
- `Numerator`: This polynomial usually has `higher degrees`.
- `Dominator`: This polynomial (or monomial/binomial) usually `lower degrees`.
- `Remainder`: After the `degrading` all the `higher degree` terms, left some terms can't be lower than the `dominator`'s degree, we then stop here, and call it remainder.

A normal division: 

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_01.png)

We can also write this division as below, which replace `R` with `+`, makes it more intuitive:

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_02.png)

Same thing we can apply to the `polynomial division`, 
Assume that there's a division: 
```javascript
f(x) ÷ d(x) = q(x) with a remainder of r(x)
```
and we can rewrite it to:

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_03.png)



Example: 
We got two polynomials need to be divided one by another, and we could represent it as below:

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_04.png)

By multiplying `x²` to `(x-3)`, we could get `x³ − 3x²`, which could be use to `cancel out` it from the `numerator`, to `degrade` it. 

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_05.png)

After the first `degrading`, it gets a `lower degree polynomial`, 
and the `left over` is still `higher` than the dominator, 
so we can repeat the same process to do it again, 
until the `left over` is `zero` or lower than the `dominator`.

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_06.png)

### Example
![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_07.png)
Solve:
![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_08.png)
![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_09.png)




## `The Remainder Theorem`

[Refer to Math is fun](http://www.mathsisfun.com/algebra/polynomials-remainder-factor.html)

> When we divide a polynomial `f(x)` by `x − c` and the remainder is `r`, then:
`r = f(c)`.

### Example
[Practice.](https://www.khanacademy.org/math/algebra2/modal/e/remainder-theorem-of-polynomials)

![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_10.png)
Solve:
![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_11.png)
![image](2018-03-19T15-44-55_`Polynomial long division`_files/img_12.png)


## `The factor theorem`




