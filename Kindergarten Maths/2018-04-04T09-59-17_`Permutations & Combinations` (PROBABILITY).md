# `Permutations & Combinations` (PROBABILITY)
> Aside from probability, `Permutations` and `Combinations` are essential tools for statistics.

They're to solve the problem: `how many groups are there of if we choose some from some.`

[Jump back to previous note: `Intro to probability`.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-372205396)

**HOW MANY** `groups` do we get if we choose a number things from the total things?
e.g., `how many groups would there be if we choose 3 people from 9 people?`

Permutations and combinations are both to count `the total number of groups`. 
We got TWO types of ways to count:
- Permutation: If the order in the group matters.
- Combination: If the order doesn't matter.

Combinations could be seen as **`FILTERED permutations`**, which filtered out all the "duplicates", or "over counted items".

e.g., We got different groups(Permutations) as "123, 132, 231, 213, 312, 321", once we filter out the over counted items, 
the `combination` is just one: `123`.

[Refer to web article.](http://www.fairlynerdy.com/permutations_and_combinations_simplified/)

## `Permutations`
> It's literarily saying the `possibilities`. 

Notice: `possibilities` ≠ `probabilities`

e.g., the `possibilities` of how to arrange three numbers 1,2,3?
It could be: `123, 132, 231, 213, 312, 321`, so answer is `6 possible ways`.
To count that algebraically, it'd be `3*2*1`, answer is `6 possible ways`.

How do we do this?

Possible ways to fit in the 1st position are 3, and we got 2 **left overs**. Then the 2nd place could have 2 possible ways, and we got 1 **left over**. So the 3rd position could be 1 possible way.

And just to logically think about it, we should MULTIPLY them together to get ALL POSSIBLE WAYS: `3*2*1`.

![image](2018-04-04T09-59-17_`Permutations & Combinations` (PROBABILITY)_files/img_01.png)


## `Combinations`

![image](2018-04-04T09-59-17_`Permutations & Combinations` (PROBABILITY)_files/img_02.png)


