#  ❖ Z Test (z statistics)

> _Z Test_ is a test constructed using the `Z-score`

[`▶︎ Jump back to previous note on: Z-score`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-410644808)
[`▶︎ Jump back to previous note on: Z-interval`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-418641425)

## Formula of 「Z Test Statistic for proportion」

[`▶︎ Jump back to previous note on: Sample Proportion`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-416493188)


The test statistic gives us an idea of how far away our sample result is from our null hypothesis. For a one-sample z-test for a proportion, our test statistic is:

![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_01.png)
(which p^ is the `Sample proportion`, p₀ is the proportion from _null hypothesis_, n is sample size)

> Understanding the formula:
The `statistic - parameter` results the DISTANCE from _Sample proportion_ to _Population proportion_.
The `Standard Deviation of statistic` represents the ~DISTANCE from _Sample SD_ to population SD.~
Therefore, dividing the **Distance of proportion** by **Distance of SD** will results in a `Normalized Distance for proportion`.


## Calculating 「Z Test」 about a proportion

[Refer to Khan academy: Calculating a z statistic in a test about a proportion](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/modal/v/calculating-a-z-statistic-in-a-significance-test)

### Example
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_02.png)
Solve:
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_03.png)



## Calculating a 「P-value」 given a z statistic

[Refer to Khan academy: Calculating a P-value given a z statistic](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/modal/v/calculating-p-value-from-z-table)


### Example
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_04.png)
Solve:
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_05.png)


### Example
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_06.png)
Solve:
- To get the probability in a Z-score normal distribution, we need:
    - Mean
    - Standard deviation
    - Z-score
- For convenience, we can set the _mean_ as `0` at the centre, and _SD_ as `1`
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_07.png)
- Since it's asking for proportion at left tail, so we can directly input those values in a calculator:
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_08.png)
- The answer is 0.106


### Example
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_09.png)
Solve:
- Get a calculator, and input these values:
    - Mean (default): 0
    - SD (default): 1
    - Z-score: -1.5
- We get that the `left-tail` proportion is `0.0668072`
- Since the alternative hypothesis is `ha ≠ ...`, so we're to calculate BOTH tails proportion.
- Z-score as `-1.5` means the point is at left tail, so we just need to multiply the proportion by `2`
- The `p-value` then is `0.0668072*2 = 0. 134`
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_10.png)



## Making conclusions in a 「z test」 for a proportion

Calculate Z-value -> Convert to P-value -> Compare with ⍺ level -> Make decision.

### Example
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_11.png)
Solve:
![image](2018-09-11T08-22-29_❖ Z Test (z statistics)_files/img_12.png)

