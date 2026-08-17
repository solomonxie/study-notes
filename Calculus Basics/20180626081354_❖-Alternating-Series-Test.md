#  ❖ Alternating Series Test

It's the test for `Alternating series`.

[►Refer to Khan academy: Alternating series test](https://www.khanacademy.org/math/ap-calculus-bc/bc-series/modal/v/alternating-series-test)
[►Refer to xaktly: Alternating Series](http://www.xaktly.com/AlternatingSeries.html)

## Alternating Series

It means,
**Terms of the series "alternate"  between positive and negative.**

etc., `The alternating harmonic series`:
![image](20180626081354_❖-Alternating-Series-Test_files/img_01.png)


## The Alternating Series Test

![image](20180626081354_❖-Alternating-Series-Test_files/img_02.png)

The very good example of this test is the `Alternating Harmonic Series`:

![image](20180626081354_❖-Alternating-Series-Test_files/img_03.png)

▲ It does **CONVERGES**. (But the Harmonic Series does NOT converge)

Strategy:
- Take AWAY the `Alternating sign (-1)ⁿ`:
![image](20180626081354_❖-Alternating-Series-Test_files/img_04.png)
- Determine if the rest part is a decreasing series:
![image](20180626081354_❖-Alternating-Series-Test_files/img_05.png)
- Take limit of the rest part:
![image](20180626081354_❖-Alternating-Series-Test_files/img_06.png)
- If `Limit = 0`, then the series **CONVERGES**.
- If `Limit ≠ 0`, then the series **DIVERGES**.



### Example
![image](20180626081354_❖-Alternating-Series-Test_files/img_07.png)
Solve:
- Notice this is an `alternating series`, so we're to apply the `alternating series test`.
- Take away the `alternating term`, and left with `(2/p)ⁿ`.
- So the series only converges if `(2/p)ⁿ` is **decreasing** and its **limit is `0`**.
- And the only way to make it decreasing is to make sure `(2/p) < 1`.
- Based on that `p` value, the limit of `(2/p)ⁿ` is surely a `0`.
- Therefore, `p > 2` makes the series converges.


### Example
![image](20180626081354_❖-Alternating-Series-Test_files/img_08.png)
Solve:
- Notice this is an `alternating series`, so we're to apply the `alternating series test`.
- Take away the `alternating term`, and left with `(2n)ᴾ`.
- So the series only converges if `(2n)ᴾ` is **decreasing** and its **limit is `0`**.
- And the only way to make it decreasing is to make sure `p < 0`.
- Based on that `p` value, the limit of `(2n)ᴾ` is surely a `0`.
- Therefore, `p < 0` makes the series converges.

