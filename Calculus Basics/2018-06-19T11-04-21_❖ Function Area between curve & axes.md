#  ❖ Function Area between curve & axes

[►Jump to Khan academy for some practice: Curve areas](https://www.khanacademy.org/math/ap-calculus-bc/bc-applications-definite-integrals/modal/quiz/bc-horizontal-area-quiz)

## Area Between 「X-axis」 & 「Curve」

Strategy:
- Figure out the interval (boundaries) for the definite integral.
- Directly Integrate the function: `ʃ f(x) dx` over the interval.

### Example
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_01.png)
Solve:
- The interval is between `0 & x when f(x)=0`.
- Set `f(x) = 0 = 2 + 2cos(x)` -> `cos(x)=-1` -> `x = arccos(-1) = π`
- So the interval is `[0, π]`.
- The area then is `ʃ (2+2cosx) dx` over the interval `[0, π]`
- The result is `2π` from the definite integral .


## Area Between 「Y-axis」 & 「Curve」

Strategy:
- Inverse the function to make it in term of `y`.
- Instead of integrate in term of `x`, we need to integrate in term of `y`.
- Integrate: `ʃ f(y) dy`



### Example
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_02.png)
Solve:
- Now we have the function `f(y) = 15/y`
- Integrate the function in term of `y`:
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_03.png)


### Example
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_04.png)
Solve:
- Integral the function in term of `y`:
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_05.png)



## Area Between 「Two curves」
 

 
Strategy:
 
- Subtract smaller area from bigger area (must be positive): `ʃ |f(x)-g(x)| dx`
 

 

 
### Example
 
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_06.png)
 
Solve:
 
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_07.png)
 

 

 
### Example
 
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_08.png)
 
Solve:
 
- The graph is as below:
 
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_09.png)
 
- We can actually ignore the graph to calculate:
 
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_10.png)
 


## 「Horizontal areas」 between curves

### Example
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_11.png)
Solve:
- Clearly, it's bit harder to find the x-axis boundaries for the area.
- And the y-axis boundaries could be easily found where as the point two curves intersect.
- So let two equations equal to get two intersect points:
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_12.png)
- And since it's area between two functions, we subtract one from another `f(y) - g(y)` to get:
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_13.png)
- So the result would be:
![image](2018-06-19T11-04-21_❖ Function Area between curve & axes_files/img_14.png)

