#  ❖ Area of 「Polar Curves」 (Integral Calc)

Calculating area for `polar curves`, means we're now under the `Polar Coordinate` to do integration.
And instead of using `rectangles`  to calculate the area, we are to use `triangles` to integrate the area for a curve.

> [`▶ Back to Polar functions (Differential Calc)`](http://github.com/solomonxie/solomonxie.github.io/issues/49#issuecomment-396527546)

![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_01.png)


There're a few notable differences for calculating `Area of Polar Curves`:
- It's now under the **`Polar Coordinate`**.
- It's using **`Circle Sectors`** with infinite small angles to integral the area.
- It's the area between the function graph and a **`RAY`** or two **`RAYS`** from the origin.

[`▶ Practice at Khan academy: Area bounded by polar curves`](https://www.khanacademy.org/math/old-ap-calculus-bc/bc-applications-definite-integrals/modal/e/area-enclosed-by-polar-graphs)

[Refer to Khan Academy: Area bounded by polar curves](https://www.khanacademy.org/math/ap-calculus-bc/bc-applications-definite-integrals/bc-polar-graphs-area/v/formula-area-polar-graph)

![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_02.png)


![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_03.png)


## Finding the right 「boundaries」

> The most tricky part in Polar system, is finding the right boundaries for `θ`, and it will be the first step for polar integral as well.

[Refer to youtube: Finding Area In Polar Coordinates](https://www.youtube.com/watch?v=GQ6cDvY8K9g)

Why is this?
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_04.png)

> Better to try out on Desmos.com, to see if the interval produces the right shape.



### Example
Find out the boundaries of θ for integrating the shaded area:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_05.png)
Solve:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_06.png)

### Example
Find out the boundaries of θ for both of the polar curves:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_07.png)
Solve:
- Obviously, for the shading area, both of the curves start at `θ = 0` and end at intersection `θ = π/6`


### Example
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_08.png)
Solve:
- Start thinking as we're drawing the graph: the `r` starts drawing at 0, all the way **down** for a round and goes back to 0.
- Since it goes **counter-clockwise**, so it's obvious `r` goes from `π` then takes a round back to `2π`.
- So the boundaries are `π and 2π`

### Example
Find out the boundaries of θ for integrating the shaded area:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_09.png)
Solve:
- Let's look at the **drawing track**: It starts at `r = -1` ends at `r = 0`.
- So we're to find out the θ-value for the start of `r` and end of `r`:
    - When `r = -1`, from the equation we get `θ = 0`
    - When `r = 0`, from the equation we get `θ = π/3`
- Therefore, the boundaries are:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_10.png)



### Example
Find out the boundaries of θ for integrating the shaded area:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_11.png)
Solve:
- Notice that, for the range `θ ∋ [0,π]`, it makes `r` negative: `sin(π)-1 = -1` and `sin(0)-1 = -1`.
- But in this case, `r` starts at 0 and ends at 0, not negative value, 
- so we're gonna **despise** the given range, and compute the θ-value for `r=0`:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_12.png)
- And the boundaries for θ is `π/6` and `5π/6`.



## Area between 「two Polar Curves」


### Example
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_13.png)
Solve:
- First to notice, the boundaries are at two function's intersects.
- So let `3sinθ = 1+sinθ`, to get `θ = π/6 and 5π/6`, which are the boundaries.
- Within the boundaries, the area asked could be calculated by subtracting the smaller area form bigger one.
- So the area is:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_14.png)



### Example
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_15.png)
Solve:
- It's bit tricky to find the boundaries.
- In this case, it's **not subtracting** one area from another, but **adding two small areas**:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_16.png)
- As showed above, for the `cosθ` shape, its boundaries are same with Quadrant-1: `[0, π/2]`
- For the `1+sinθ` shape, its boundaries are same with Quadrant-4: `[3π/2, 2π]`
- So the shaded region is:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_17.png)


### Example
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_18.png)
Solve:
- Another tricky one to **combine** areas.
- Figure out the combination areas as below:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_19.png)
- So the total area is:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_20.png)


### Example
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_21.png)
Solve:
![image](2018-06-20T07-50-23_❖ Area of 「Polar Curves」 (Integral Calc)_files/img_22.png)

