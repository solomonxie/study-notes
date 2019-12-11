# Unpack a list of tuples

```py
>> arr = [(1,2,(3,4)), (5,6,(7,8))]
>> for i, (a,b,(c,d)) in enumerate(arr):
>>    print(i,a,b,c,d)
0 1 2 3 4
1 5 6 7 8
```
