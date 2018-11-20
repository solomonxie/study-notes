# `Hash Tables` (Data structure)

![image](2018-11-20T06-40-19_`Hash Tables` (Data structure)_files/img_01.png)

## ADT DEFINITION

```py
ADT: <HASH TABLE>

    It's actually a MAP data structure, that contains key / value pairs. 
    It uses a <hash function> to compute an index into an array of buckets or slots, 
    from which the desired value can be found.

    A Hash Table is a data structure that uses a hash function to 
    efficiently map keys to values (Table or Map ADT), 
    for efficient search/retrieval, insertion, and/or removals.
    Hash Table is widely used in many kinds of computer software, 
    particularly for associative arrays, database indexing, caches, and sets.

    The hash function should always give the same output number for the same input.

DATA:
    - Keys []
        - key     # a string as the key
    - Map []
        - index   # the pointer to the actual value
        - value

OPERATIONS:

    hash(key):
        (*) return the index of the actual value with respect to the key.

    add(key, value):
        (*) 

    lookup(key):
        (*) 

    remove(key):
        

```


## IMPLEMENTATION

[Refer to Beau Carnes: Hash Table (JS)](https://codepen.io/beaucarnes/pen/VbYGMb?editors=0011)

## ANALYSIS

![image](2018-11-20T06-40-19_`Hash Tables` (Data structure)_files/img_02.png)

