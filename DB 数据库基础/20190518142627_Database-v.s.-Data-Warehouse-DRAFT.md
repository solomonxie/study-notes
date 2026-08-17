# Database v.s. Data Warehouse [DRAFT]

terms: OLAP cube, OLTP, data cube, MDX query, multidimensional data model, multidimensional analysis, Dimensional Modeling

https://www.youtube.com/watch?v=zTs5zjSXnvs
https://www.youtube.com/watch?v=2ryG3Jy6eIY
https://www.wikiwand.com/en/Dimensional_modeling

> The purpose of Data Warehousing is to provide aggregate data(total, average..) which is in a suitable format for decision making.


- old: OLTP - Online Transaction Processing - slow, not flexible to navigate
- new: OLAP - Online Analytical Processing - designed to navigate super fast by preprocessing & storing every possible combination of dimensions, measures, and hierarchies before users query.
- newer: Dimensional Relational Model - not pre-calculate but processing data at runtime

[Dimensional Modeling:](https://www.wikiwand.com/en/Dimensional_modeling)
> Dimensional modeling always uses the concepts of facts (measures), and dimensions (context). 
Facts are typically (but not always) numeric values that can be aggregated, and dimensions are groups of hierarchies and descriptors that define the facts.

Dimensional modeling does not necessarily involve a relational database. The same modeling approach, at the logical level, can be used for any physical form, such as multidimensional database or even flat files. 
