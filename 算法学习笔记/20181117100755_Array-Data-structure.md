# `Array` (Data structure)



## ADT DEFINITION

```py
ADT: <ARRAY>

    It's an array of values with basic data types;
    All values stored in the memory are next to each other.
    It looks like: a1, a2, a3 ...... an.

DATA:
    - values []           # actual data stored in an array 
    - starting_address    # Starting memory address: 0x0023101131
    - maximum_size        # Storage size: like 8 bits, 32 bits
    - length              # How many elements

OPERATIONS:

    __init__(size):
        create memory space for a size for the list.

    getElementAt(index):
        (*) return the value at a certain index.

    getPositionOf(value):
        (*) return the index for the value.

    insertElementAt(value, index):
        (*) insert the value at a certain index.

    deleteElementAt(index):
        (*) delete the element at a certain index.

```

## IMPLEMENTATION


## ANALYSIS
