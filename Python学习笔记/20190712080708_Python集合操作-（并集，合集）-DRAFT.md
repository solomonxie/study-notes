# Python集合操作 （并集，合集） [DRAFT]

Refer to: https://docs.python.org/2/library/sets.html
Refer to: https://stackoverflow.com/questions/16579085/python-verifying-if-one-list-is-a-subset-of-the-other

```sh
# 差集
>>> set([1,2]) & set([1,2,3])
set([1, 2])
>>> set([0]) & set([1,2,3])
set([])
```


Operation | Equivalent | Result
-- | -- | --
len(s) |   | number of elements in set s (cardinality)
x in s |   | test x for membership in s
x not in s |   | test x for non-membership in s
s.issubset(t) | s <= t | test whether every element in s is in t
s.issuperset(t) | s >= t | test whether every element in t is in s
s.union(t) | s \| t | new set with elements from both s and t
s.intersection(t) | s & t | new set with elements common to s and t
s.difference(t) | s - t | new set with elements in s but not in t
s.symmetric_difference(t) | s ^ t | new set with elements in either s or t but not both
s.copy() |   | new set with a shallow copy of s


