# `Queue` (Data structure)

[Refer to wiki: Queue (abstract data type)](https://www.wikiwand.com/en/Queue_(abstract_data_type))

![image](2018-11-19T15-21-49_`Queue` (Data structure)_files/img_01.png)


## ADT DEFINITION

> "There are several efficient implementations of FIFO queues. An efficient implementation is one that can perform the operations—enqueuing and dequeuing—in O(1) time."

Linked list implementation of Queue:
```py
ADT: <QUEUE> (linked list)

DATA:
    - Node
        - value
        - next
    - Queue
        - root
        - length

OPERATIONS:

    __init__():

    enqueue(value):
        (*) add the new element to the last

    dequeue():
        (*) delete the first element
```

Array implementation of Queue:
```py
ADT: <QUEUE> (array)

DATA:
    - Queue
        - elements []
        - head
        - tail
```


## IMPLEMENTATION


## ANALYSIS

![image](2018-11-19T15-21-49_`Queue` (Data structure)_files/img_02.png)

