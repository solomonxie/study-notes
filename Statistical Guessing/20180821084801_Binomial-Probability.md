# Binomial Probability

[Refer to article on Khan academy: Binomial probability (basic)](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/modal/a/binomial-probability-basic)
[Refer to Khan academy: Generalizing k scores in n attempts](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/modal/v/generalizing-k-scores-in-n-attempts)

[`▶︎ Online Binomial Probability Calculator`](https://www.omnicalculator.com/statistics/binomial-distribution)

## Formula of 「Binomial Probability」


![image](20180821084801_Binomial-Probability_img_01.png)


![image](20180821084801_Binomial-Probability_img_02.png)


We could simplify (verbal) it as:
```
P(X=r) = Combinations × P(yes) × P(no)
```

For the **combinations**, here's the formula:
![image](20180821084801_Binomial-Probability_img_03.png)

Or use the [`▶︎ Online Combination Calculator`](https://www.omnicalculator.com/statistics/combination).


Example:
![image](20180821084801_Binomial-Probability_img_04.png)

### Example
![image](20180821084801_Binomial-Probability_img_05.png)
Solve:
- Apply the `Binomial Probability Formula`, the answer is:
![image](20180821084801_Binomial-Probability_img_06.png)


## 「Mean & Variance」 of Binomial R.V.

![Formula](20180821084801_Binomial-Probability_img_07.png)

- `Expected Value = Mean = μx`
- `Variance = Standard Deviation = σx`


### Example
![image](20180821084801_Binomial-Probability_img_08.png)
Solve:
![image](20180821084801_Binomial-Probability_img_09.png)


### Example
![image](20180821084801_Binomial-Probability_img_10.png)
Solve:
- `Mean = μx = np = 100 * 0.25 = 25`
- `SD = σx = √(np(1-p)) = √(25*0.75) = 4.33`


## 「Cumulative Binomial Probability」


### Example
![image](20180821084801_Binomial-Probability_img_11.png)
Solve:
- One way:
![image](20180821084801_Binomial-Probability_img_12.png)
- Another way:
![image](20180821084801_Binomial-Probability_img_13.png)


### Example
![image](20180821084801_Binomial-Probability_img_14.png)
Solve:
- We can see it as `P(X > 3) = P(4) + P(5)`, or `P(X>3) = 1 - (P(1) + P(2) + P(3))`, we're gonna use first one in this case.
![image](20180821084801_Binomial-Probability_img_15.png)

